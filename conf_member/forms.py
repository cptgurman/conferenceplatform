from django.forms import ModelForm, widgets
from django.forms.fields import DateField
from core.models import MemberInfo, Conference, MemberApplication, ConferenceSections
from django import forms
from django.forms.models import inlineformset_factory, modelform_factory, modelformset_factory
import datetime


class lkUser(ModelForm):
    class Meta:
        model = MemberInfo
        fields = "__all__"
        widgets = {
            'memberinfo_user': forms.HiddenInput(),
            'memberinfo_surname': forms.TextInput(attrs={'class': 'member'}),
            'memberinfo_name': forms.TextInput(attrs={'class': 'member'}),
            'memberinfo_otchestvo': forms.TextInput(attrs={'class': 'member'}),
            'memberinfo_dateofbirth': forms.SelectDateWidget(years=range(datetime.datetime.today().year-10,datetime.datetime.today().year-80,-1),attrs={'class': 'data'}),
            'memberinfo_telephone': forms.TextInput(attrs={'class': 'member'}),
            'memberinfo_job_telephone': forms.TextInput(attrs={'class': 'member'}),
            'memberinfo_dolshnost': forms.TextInput(attrs={'class': 'member'}),
            'memberinfo_education': forms.TextInput(attrs={'class': 'member'}),
            'memberinfo_achievements': forms.TextInput(attrs={'class': 'member'}),
            'memberinfo_male': forms.Select(attrs={'class': 'member'}),
            'memberinfo_OKS': forms.TextInput(attrs={'class': 'member'}),
            'memberinfo_DOPOKS': forms.TextInput(attrs={'class': 'member'}),
            'memberinfo_OKVED': forms.TextInput(attrs={'class': 'member'}),
            'memberinfo_gradee': forms.Select(attrs={'class': 'member'}),
            'memberinfo_gradee_name': forms.Select(attrs={'class': 'member'}),
        }
   
       
class MemberCreateApplication(ModelForm):
    class Meta:
        model = MemberApplication
        fields = "__all__"
        widgets = {
            'member': forms.HiddenInput(),
            'conference_id': forms.HiddenInput(),
            'speech_file': forms.FileInput(attrs={'class': 'application'}),
            'app_status': forms.HiddenInput(),
            'expert_app_comment': forms.HiddenInput(),
            'participation_form': forms.Select(attrs={'class': 'application'}),
            'member_section': forms.Select(attrs={'class': 'application'}),
            'expert': forms.HiddenInput(),
            'co_authors': forms.Textarea(attrs={'class': 'application'}),
            'speech_name': forms.TextInput(attrs={'class': 'application'}),
            'speech_keywords': forms.TextInput(attrs={'class': 'application'}),
            'speech_annotation': forms.Textarea(attrs={'class': 'application'}),
            'hotel_required': forms.CheckboxInput(attrs={'class': 'application'}),
            'invitation_required': forms.CheckboxInput(attrs={'class': 'application'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        conference = Conference.objects.get(id=self.initial['conference_id']) 
        self.fields['member_section'].queryset = ConferenceSections.objects.filter(conference_sections_conference_id=conference)


class MemberUpdateApplication(ModelForm):
    class Meta:
        model = MemberApplication
        fields = ['speech_file']
        widgets = {
            'speech_file': forms.FileInput(attrs={'class': 'Updateapplication'}),        
        }      
