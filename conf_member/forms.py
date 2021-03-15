from django.forms import ModelForm, widgets
from django.forms.fields import DateField
from core.models import MemberInfo, Conference, MemberApplication
from django import forms
from django.forms.models import inlineformset_factory, modelform_factory, modelformset_factory


class lkUser(ModelForm):
    class Meta:
        model = MemberInfo
        fields = "__all__"
        widgets = {
            'memberinfo_user': forms.HiddenInput(),
            'memberinfo_surname': forms.TextInput(attrs={'class': 'member'}),
            'memberinfo_name': forms.TextInput(attrs={'class': 'member'}),
            'memberinfo_otchestvo': forms.TextInput(attrs={'class': 'member'}),
            'memberinfo_dateofbirth': forms.SelectDateWidget(attrs={'class': 'data'}),
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
        # 'member_file': forms.FileField(),
        'member_name': forms.HiddenInput(),
        'member_application_status': forms.HiddenInput(),
        'member_application_comment': forms.HiddenInput(),
        }