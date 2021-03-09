from django.shortcuts import render
from core.models import Conference
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.list import ListView
from .forms import ConferenceEditForm, ConferenceFormset
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.forms import formset_factory
from django.db import transaction



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

    def form_valid(self, form):
        context = self.get_context_data()
        sections = context['sections']
        self.object = form.save()
        if sections.is_valid():
            sections.instance = self.object
            sections.save()
        return super().form_valid(form)


    


    