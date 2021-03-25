from django.shortcuts import render, redirect
from core.models import Conference, ConferenceSections, MemberApplication
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.list import ListView

from django.contrib.auth.mixins import PermissionRequiredMixin
from django.forms import formset_factory
from django.db import transaction
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse_lazy
from .forms import ExpertReview

class ArticlesForReview(ListView):
    model = MemberApplication
    def get_queryset(self):
        qs = super().get_queryset() 
        return qs.filter(expert=self.request.user)


class ExpertArticleReview(UpdateView):
    model = MemberApplication
    form_class = ExpertReview