from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from core.models import MemberApplication, MemberInfo, Conference, Member, ExpertKeywords, User
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.list import ListView
from django.views.generic.base import TemplateView
from .forms import  lkUser, MemberCreateApplication, MemberUpdateApplication
import os
import re
import docx
import nltk
from nltk.corpus import stopwords
from rutermextract import TermExtractor
 
nltk.download('stopwords')

class lk(ListView):
    model = Conference
    def lk(self, request):
        return render(request, "registration/lk.html")


class MemberDataUpdate(UpdateView):
    model=MemberInfo
    form_class = lkUser


class MemberDataCreate(CreateView):
    model=MemberInfo
    form_class = lkUser

    def get_initial(self):
        initial = super().get_initial()
        initial['memberinfo_user'] = self.request.user
        return initial


class MemberConfsList(ListView):
    model=MemberApplication
    template_name = 'conf_member/MyConfs.html'
    def get_queryset(self):
        qs = super().get_queryset() 
        return qs.filter(member=self.request.user).order_by('-conference_id__conference_date_start', 'conference_id__conference_name')


class MemberUpdateApplicationView(UpdateView):
    model=MemberApplication
    form_class = MemberUpdateApplication
    template_name = 'conf_member/UpdateApplication.html'
    success_url = reverse_lazy('member_confs')

class MemberCreateApplicationView(CreateView):
    model=MemberApplication
    form_class = MemberCreateApplication
    template_name = 'conf_member/CreateApplication.html'
    success_url = reverse_lazy('member_confs')
    
    def get_initial(self,*args, **kwargs):
        initial = super().get_initial()
        initial['member'] = self.request.user
        initial['conference_id']=self.kwargs['conf_id']
        return initial

    def post(self, request, *args, **kwargs):
        super().post(request)
        member_speech_file = request.FILES['speech_file']
        docx_speech_file= docx.Document(member_speech_file)

        speech_text = []
        for paragraph in docx_speech_file.paragraphs:
            speech_text.append(paragraph.text)
        speech_text_spisok=' '.join(speech_text)

        speech_text_split=speech_text_spisok.split()     
        punctuation=re.sub(r'[^A-Za-z0-9а-яА-Я]+',' ',str(speech_text_split)) #убираем мусор
        punctuation2=re.sub(r'\b\w{1,3}\b', ' ', punctuation) #убираем слова меньше 3 букв
        punctuation_low = list(punctuation2.lower().split()) #убираем заглавные буквы
        # сюда стоп слова
        filtered_speech = []
        for word in punctuation_low:
            if word not in stopwords.words("russian"):
                filtered_speech.append(word)


        experts_count = len(ExpertKeywords.objects.all())
        i = 0
        match = 0
        keywords_list = []
        expert_list = []
        while i < experts_count:
            for expert_keywords in ExpertKeywords.objects.all()[i].keywords.split():
                expert_name = ExpertKeywords.objects.all()[i].expert
                for member_keywords in filtered_speech:
                    if expert_keywords == member_keywords:
                        match += 1
            keywords_list.append(match)
            expert_list.append(str(expert_name))
            match = 0
            i += 1
            
        max_match = keywords_list.index(max(keywords_list))

        t = User.objects.all()[max_match].id
        
        MemberApplication.objects.update(member=self.request.user, expert=t)

        return redirect('lk')


    