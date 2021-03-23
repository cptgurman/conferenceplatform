from django.shortcuts import render, redirect
from core.models import MemberApplication, MemberInfo, Conference, Member
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.list import ListView
from django.views.generic.base import TemplateView
from .forms import  lkUser, MemberCreateApplication
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
    

class MemberCreateApplicationView(CreateView):
    form_class = MemberCreateApplication
    template_name = 'conf_member/application.html'
    success_url='myconf'
    
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

        speech_string= ' '.join(filtered_speech)
        


        speech_keywords=[]
        term_extractor = TermExtractor()
        for term in term_extractor(speech_string):
            if term.count>4:
                speech_keywords.append(term.normalized)
        print (speech_keywords)


        # # for gdfhdfgjoxhb in slova:
        # #     fff = str(gdfhdfgjoxhb)
        # #     a = fff.replace(" ", "_") 
        # #     slova1.append(a)

        # print (slova)

        # schet=-1
        # spisok=[]
        # spisokproc=[]
        # i=0

        # dir = 'D:/Рабочий стол/adasd/adasd/textsssss'
        # papki = os.listdir(dir)       
        # kolvo=len(spisoksplit)
        # dfg =[]

        # for papka in papki:
        #     schet+=1 
        #     schet2=0
        #     kolvopapki=0
        #     dir2 = 'D:/Рабочий стол/adasd/adasd/textsssss'+'/{}'.format(papki[schet])
        #     papki2 = os.listdir(dir2)
        #     kolvopapkishet = len(papki2)


        #     for papka2 in papki2:
        #         if kolvopapki<kolvopapkishet:
        #             sovpalo=0
        #             os.chdir('D:/Рабочий стол/adasd/adasd/textsssss'+'/{}'.format(papki[schet])+'/{}'.format(papki2[schet2]))
        #             f = codecs.open('D:/Рабочий стол/adasd/adasd/textsssss'+'/{}'.format(papki[schet])+'/{}'.format(papki2[schet2])+'/text.txt', 'r', 'utf8')
        #             Text=f.read()
        #             f.close()
        #             splitslov = Text.split()
        #             listslov = list(splitslov)

        #             for elementspisok in slova:
        #                 fff = len(str(elementspisok).split())
        #                 tt = 0
        #                 yy = fff
        #                 # print ("elementspisok     " + str(elementspisok))

        #                 for elementext in listslov:
        #                     elementext2 = listslov[tt:yy]
        #                     fgdfgh = " ".join(elementext2)
        #                     tt += fff
        #                     yy += fff
        #                     # print ("fgdfgh     " + str(fgdfgh))


        #                     if fgdfgh == elementspisok:
        #                         sovpalo+=1
        #                     # print (sovpalo)

                               
                    
        #             if sovpalo>2:
        #                 spisok.append('Коференция: '+papki[schet]+' '+'Направление: '+papki2[schet2])
                    
        #             schet2+=1 
        #             kolvopapki+=1
        #         else:
        #             schet+=1 
        #             schet2=0
  


        # spisok1=list(set(spisok))
        # spisokfinale='\n'.join(spisok1)

        # self.textBrowser.setText(spisokfinale)

        return redirect('lk')


    