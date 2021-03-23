from django.shortcuts import render, redirect
from core.models import MemberApplication, MemberInfo, Conference, Member
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.list import ListView
from django.views.generic.base import TemplateView
from .forms import  lkUser, MemberCreateApplication
import os


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
        member_speech_file=request.POST.get('speech_file')
        os.startfile(f'C:/develope/conferenceplatform/media/{member_speech_file}')
        return redirect('myconf')
    

    