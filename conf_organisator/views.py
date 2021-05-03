from django.shortcuts import render, redirect
from core.models import Conference, ConferenceSections
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.list import ListView
from .forms import ConferenceEditForm, ConferenceFormset
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.forms import formset_factory
from django.db import transaction
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse_lazy
import sqlite3
import re


# Create your views here.
class ConferenceUpdate(PermissionRequiredMixin, UpdateView):
    form_class = ConferenceEditForm
    model = Conference
    permission_required = 'core.add_conference'
    success_url = reverse_lazy('myconf')

    def get_context_data(self, *args, **kwargs):
        data1 = super().get_context_data()
        data1['sections'] = ConferenceFormset(instance=self.object)
        data1['qs'] = ConferenceSections.objects.all().filter(
            conference_sections_conference_id=self.object)

        # Запрос sql
        conn = sqlite3.connect('db.sqlite3')
        cur = conn.cursor()
        cur.execute(
            "SELECT COUNT(member_id) FROM core_memberapplication GROUP BY member_section_id")

        counts = [x[0] for x in cur.fetchall()]
        data1['counts'] = counts
        return data1

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        formset = ConferenceFormset(request.POST, instance=self.object)

        if formset.is_valid():
            return self.form_valid(formset)
        else:
            print(formset.errors)
            return self.form_invalid(formset)

    def form_valid(self, formset):
        formset.instance = self.object
        formset.save()
        return redirect('myconf')


class ConferenceListView(ListView):
    model = Conference

    def get_queryset(self):
        qs = super().get_queryset()
        return qs.filter(conference_org_id=self.request.user)


class ConferenceCreate(PermissionRequiredMixin, CreateView):
    form_class = ConferenceEditForm
    permission_required = 'core.add_conference'

    def get_initial(self, *args, **kwargs):
        initial = super().get_initial()
        initial['conference_org_id'] = self.request.user
        return initial

    def get_context_data(self, *args, **kwargs):
        data = super().get_context_data()
        data['sections'] = ConferenceFormset()
        return data

    def post(self, request, *args, **kwargs):
        self.object = None
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        formset = ConferenceFormset(self.request.POST)
        if (form.is_valid() and formset.is_valid()):
            return self.form_valid(form, formset)
        else:
            return self.form_invalid(form, formset)

    def form_valid(self, form, formset):
        self.object = form.save()
        formset.instance = self.object
        formset.save()
        return redirect('myconf')
