from django.shortcuts import render, redirect
from core.models import  MemberApplication, ExpertArticle, ExpertKeywords
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.list import ListView
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.forms import formset_factory
from django.db import transaction
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse_lazy
from .forms import ExpertReview, ExpertArticleUploadForm
import docx
import re
import nltk
from nltk.corpus import stopwords
from rutermextract import TermExtractor
from numpy import unique
 

class ArticlesForReview(ListView):
    model = MemberApplication
    def get_queryset(self):
        qs = super().get_queryset() 
        return qs.filter(expert=self.request.user)


class ExpertArticleReview(UpdateView):
    success_url = reverse_lazy('articles_for_review')
    model = MemberApplication
    form_class = ExpertReview

    
class ExpertArticleUpload(CreateView):
    model=ExpertArticle
    form_class=ExpertArticleUploadForm
    success_url='myconf'

    def get_initial(self, *args, **kwargs):
        initial = super().get_initial()
        initial['expert'] = self.request.user
        return initial

    def post(self, request, *args, **kwargs):
        super().post(request)
        member_speech_file = request.FILES['article']
        docx_speech_file= docx.Document(member_speech_file)
        member_keywords_field=request.POST['article_keywords']
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

        speech_string= ' '.join(filtered_speech)
        


        speech_keywords=[] #слова из файла со статьей
        term_extractor = TermExtractor()
        for term in term_extractor(speech_string):
            if term.count>4:
                speech_keywords.append(term.normalized)

        speech_keywords_split=member_keywords_field.split()
        speech_keywords=speech_keywords+speech_keywords_split
        speech_keywords_finale=' '.join(speech_keywords) 
        speech_keywords_finale_split=speech_keywords_finale.split() #список ключевых слов статьи
        ExpertArticle.objects.update(expert=self.request.user, article_keywords=speech_keywords_finale_split)#ключевые слова текущей статьи


        expert_keywords_list=ExpertKeywords.objects.all()
        expert_keywords_list_split=expert_keywords_list[0].keywords.split()#ключевые слова эксперта


        article_keywords_list=[] #переборка всех слов в цикле
        for expert_keywords in expert_keywords_list_split:
            for article_keywords in speech_keywords_finale_split:
                if expert_keywords != article_keywords:
                    article_keywords_list.append(article_keywords)
                    
        article_keywords_list=article_keywords_list+expert_keywords_list_split #объединяем два списка
        article_keywords_list_unique=unique(article_keywords_list)#убираем повторяющиеся
        article_keywords_list_join=' '.join(article_keywords_list_unique)#пробелы между слов для текста
        ExpertKeywords.objects.update(expert=self.request.user, keywords=article_keywords_list_join) #обновление ключевых слов эксперта

        return redirect('articles_for_review')