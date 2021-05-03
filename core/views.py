from django.shortcuts import render
from core.models import Conference
from django.views.generic.list import ListView


class ConfList(ListView):
    model = Conference
    template_name = 'conf_list.html'

    def get_queryset(self):
        qs = super().get_queryset()
        return qs.order_by()
