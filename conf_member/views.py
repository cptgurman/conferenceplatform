from django.db import models
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect, request
from django.urls import reverse_lazy
from core.models import MemberApplication, MemberInfo, Conference, Member, ExpertKeywords, User, ConferenceSections
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.list import ListView
from django.views.generic.base import TemplateView
from .forms import lkUser, MemberCreateApplication, MemberUpdateApplication
import re
import docx
import nltk
from nltk.corpus import stopwords
import sqlite3


# nltk.download('stopwords')


class ConferenceInfo(TemplateView):
    model = Conference
    template_name = 'conf_member/conference_info.html'

    def get_context_data(self, *args, **kwargs):
        data = super().get_context_data()
        data['conf_info'] = Conference.objects.all().filter(
            id=self.kwargs['conf_id'])
        data['qs'] = ConferenceSections.objects.all().filter(
            conference_sections_conference_id=self.kwargs['conf_id'])
        conn = sqlite3.connect('db.sqlite3')
        cur = conn.cursor()
        cur.execute(
            "SELECT COUNT(member_id) FROM core_memberapplication GROUP BY member_section_id")

        counts = [x[0] for x in cur.fetchall()]
        data['counts'] = counts
        return data


class MemberDataUpdate(UpdateView):
    model = MemberInfo
    form_class = lkUser
    success_url = reverse_lazy('lk')


class MemberDataCreate(CreateView):
    model = MemberInfo
    form_class = lkUser
    success_url = reverse_lazy('lk')

    def get_initial(self):
        initial = super().get_initial()
        initial['memberinfo_user'] = self.request.user
        return initial


class MemberConfsList(ListView):
    model = MemberApplication
    template_name = 'conf_member/lk.html'

    def get_queryset(self):
        qs = super().get_queryset()
        return qs.filter(member=self.request.user).order_by('-conference_id__conference_date_start', 'conference_id__conference_name')


class MemberUpdateApplicationView(UpdateView):
    model = MemberApplication
    form_class = MemberUpdateApplication
    template_name = 'conf_member/UpdateApplication.html'
    success_url = reverse_lazy('member_confs')

    def post(self, request, *args, **kwargs):
        MemberApplication.objects.update(
            member=self.request.user, app_status='Consideration')
        return redirect('member_confs')


class MemberCreateApplicationView(CreateView):
    model = MemberApplication
    form_class = MemberCreateApplication
    template_name = 'conf_member/CreateApplication.html'
    success_url = reverse_lazy('member_confs')

    def get_initial(self, *args, **kwargs):
        initial = super().get_initial()
        initial['member'] = self.request.user
        initial['conference_id'] = self.kwargs['conf_id']
        return initial

    def post(self, request, *args, **kwargs):
        super().post(request)
        member_speech_file = request.FILES['speech_file']
        docx_speech_file = docx.Document(member_speech_file)

        speech_text = []
        for paragraph in docx_speech_file.paragraphs:
            speech_text.append(paragraph.text)
        speech_text_spisok = ' '.join(speech_text)

        speech_text_split = speech_text_spisok.split()
        punctuation = re.sub(r'[^A-Za-z0-9а-яА-Я]+', ' ',
                             str(speech_text_split))  # убираем мусор
        # убираем слова меньше 3 букв
        punctuation2 = re.sub(r'\b\w{1,3}\b', ' ', punctuation)
        # убираем заглавные буквы
        punctuation_low = list(punctuation2.lower().split())
        # сюда стоп слова
        filtered_speech = []
        for word in punctuation_low:
            if word not in stopwords.words("russian"):
                filtered_speech.append(word)

        experts_count = len(ExpertKeywords.objects.all())
        current_expert_number = 0
        match = 0
        keywords_list = []
        expert_list = []
        while current_expert_number < experts_count:
            # кварисэт ключевых слов для текущего эксперта и их разделение
            for expert_keywords in ExpertKeywords.objects.all()[current_expert_number].keywords.split():
                expert_name = ExpertKeywords.objects.all()[
                    current_expert_number].expert
                for member_keywords in filtered_speech:
                    if expert_keywords == member_keywords:
                        match += 1
            keywords_list.append(match)
            expert_list.append(str(expert_name))
            match = 0
            current_expert_number += 1

        max_match = keywords_list.index(max(keywords_list))
        expert_login = ExpertKeywords.objects.all()[max_match].expert

        t = User.objects.get(username=expert_login)
        MemberApplication.objects.filter(
            member=self.request.user).update(expert=t.id)

        return redirect('lk')


class Search(ListView):
    model = Conference
    template_name = "search.html"

    def get_queryset(self):

        return Conference.objects.filter(conference_full_name__icontains=self.request.GET.get("search"))


class RecomendationList(ListView):
    model = Conference
    template_name = 'conf_member/RecommendationList'

    def get(self, request):
        member_speech_text = request.GET['text_field']
        member_speech_text_split = member_speech_text.split()

        punctuation = re.sub(r'[^A-Za-z0-9а-яА-Я]+', ' ',
                             str(member_speech_text_split))  # убираем мусор
        # убираем слова меньше 3 букв
        punctuation2 = re.sub(r'\b\w{1,3}\b', ' ', punctuation)
        # убираем заглавные буквы
        punctuation_low = list(punctuation2.lower().split())
        # сюда стоп слова
        filtered_speech = []
        for word in punctuation_low:
            if word not in stopwords.words("russian"):
                filtered_speech.append(word)
        print(filtered_speech)
        return member_speech_text


class Recomendation(TemplateView):
    template_name = "conf_member/Recommendation.html"
