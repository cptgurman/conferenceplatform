from django.shortcuts import render
from core.models import Conference
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.list import ListView
from .forms import ConferenceEditForm, ConferenceFormset
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.forms import formset_factory
from django.db import transaction
from django.http import HttpResponse, HttpResponseRedirect



# Create your views here.
class ConferenceUpdate(UpdateView):
    form_class=ConferenceEditForm
    model= Conference


class ConferenceListView(ListView):
    model = Conference
    def get_queryset(self):
        qs = super().get_queryset() 
        return qs.filter(conference_org_id=self.request.user)


class ConferenceCreate(PermissionRequiredMixin, CreateView):
    form_class=ConferenceEditForm   
    permission_required = 'core.add_conference'
    
    
    def get_initial(self):
        initial = super().get_initial()
        initial['conference_org_id'] = self.request.user
        return initial

    def get_context_data(self):
        data = super().get_context_data()
        data['sections'] = ConferenceFormset()
        return data

    def post(self, request):
        # formset = ConferenceFormset(request.POST)
        form=self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        self.object = form.save()
        
        return super().form_valid(form)
        
    
       

    


    