from django.shortcuts import render
from core.models import Conference
from django.views.generic.list import ListView

class HomePage(ListView):
    model = Conference
    def get_queryset(self):
        qs = super().get_queryset() 
        return qs