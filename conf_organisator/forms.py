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
            'conference_org_id': forms.HiddenInput(),
            'conference_name': forms.TextInput(attrs={'class': 'konf'}),
            'conference_full_name': forms.TextInput(attrs={'class': 'konf'}),
            'conference_discription': forms.Textarea(attrs={'class': 'konf'}),
            'conference_date_start': forms.SelectDateWidget(attrs={'class': 'data'}),
            'conference_date_end':forms.SelectDateWidget(attrs={'class': 'data'}),
            'conference_date_reg_start': forms.SelectDateWidget(attrs={'class': 'data'}),
            'conference_date_reg_end': forms.SelectDateWidget(attrs={'class': 'data'}),
            'conference_format_id': forms.Select(attrs={'class': 'konf'}),
            'conference_faculty_id': forms.Select(attrs={'class': 'konf'}),
            'conference_building_id': forms.Select(attrs={'class': 'konf'}),
        }



ConferenceFormset = inlineformset_factory(Conference, ConferenceSections, fields = "__all__", widgets = {
            'conference_sections_conference_id': forms.HiddenInput(),
            'conference_sections_name': forms.TextInput(attrs={'class': 'konf'}),
        }, extra=1)

