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
            'memberinfo_surname': forms.TextInput(attrs={'class': 'memberinfo', "placeholder": "Фамилия"}),
            'memberinfo_name': forms.TextInput(attrs={'class': 'memberinfo', "placeholder": "Имя"}),
            'memberinfo_otchestvo': forms.TextInput(attrs={'class': 'memberinfo', "placeholder": "Отчество"}),
            'memberinfo_dateofbirth': forms.SelectDateWidget(years=range(datetime.datetime.today().year-10, datetime.datetime.today().year-80, -1), attrs={'class': 'memberinfo_dateofbirth'}),
            'memberinfo_telephone': forms.TextInput(attrs={'class': 'memberinfo', "placeholder": "Мобильный телефон"}),
            'memberinfo_education': forms.Select(attrs={'class': 'memberinfo', "placeholder": "Образование"}),
            'memberinfo_male': forms.Select(attrs={'class': 'memberinfo', "placeholder": "Пол"}),
            'memberinfo_gradee': forms.Select(attrs={'class': 'memberinfo', "placeholder": "Ученая степень"}),
            'memberinfo_gradee_name': forms.Select(attrs={'class': 'memberinfo', "placeholder": "Ученое звание"}),
            'member_photo': forms.FileInput(attrs={'class': 'member_photo', 'label': 'Ваша фотография'})
        }


class MemberCreateApplication(ModelForm):
    class Meta:
        model = MemberApplication
        fields = "__all__"
        widgets = {
            'member': forms.HiddenInput(),
            'conference_id': forms.HiddenInput(),
            'speech_file': forms.FileInput(attrs={'class': 'file_input'}),
            'app_status': forms.HiddenInput(),
            'expert_app_comment': forms.HiddenInput(),
            'participation_form': forms.Select(attrs={'class': 'memberinfo'}),
            'member_section': forms.Select(attrs={'class': 'memberinfo'}),
            'expert': forms.HiddenInput(),
            'co_authors': forms.Textarea(attrs={'class': 'memberinfo', "placeholder": "Введите соавторов"}),
            'speech_name': forms.TextInput(attrs={'class': 'memberinfo', "placeholder": "Введите название статьи"}),
            'speech_keywords': forms.TextInput(attrs={'class': 'memberinfo', "placeholder": "Введите ключевые слова статьи"}),
            'speech_annotation': forms.Textarea(attrs={'class': 'memberinfo', "placeholder": "Введите аннотацию статьи"}),
            'hotel_required': forms.CheckboxInput(attrs={'class': 'memberinfo'}),
            'invitation_required': forms.CheckboxInput(attrs={'class': 'memberinfo'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        conference = Conference.objects.get(id=self.initial['conference_id'])
        self.fields['member_section'].queryset = ConferenceSections.objects.filter(
            conference_sections_conference_id=conference)


class MemberUpdateApplication(ModelForm):
    class Meta:
        model = MemberApplication
        fields = ['speech_file']
        widgets = {
            'speech_file': forms.FileInput(attrs={'class': 'Updateapplication'}),
        }
