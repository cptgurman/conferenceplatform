from django.forms import ModelForm, widgets, modelformset_factory, formset_factory, inlineformset_factory
from django.contrib.auth.forms import  UserChangeForm, UserCreationForm
from django.contrib.auth.models import User
from django.forms.fields import DateField
from core.models import Conference, ConferenceSections
from django import forms



class ConferenceEditForm(ModelForm):
    
    class Meta:
        model = Conference
        fields = "__all__"
        widgets = {
        'conference_date_start': forms.SelectDateWidget,
        'conference_date_end':forms.SelectDateWidget,
        'conference_date_reg_start': forms.SelectDateWidget,
        'conference_date_reg_end': forms.SelectDateWidget,
        'org_id': forms.HiddenInput,
        }


ConferenceFormset = inlineformset_factory(Conference, ConferenceSections, fields = "__all__")

