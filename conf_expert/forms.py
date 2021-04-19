from django.forms import ModelForm, widgets
from core.models import MemberApplication, ExpertArticle
from django import forms



class ExpertReview(ModelForm):
    class Meta:
        model = MemberApplication
        fields = ['app_status', 'expert_app_comment']
        widgets = {
             
        #     'conference_name': forms.TextInput(attrs={'class': 'konf'}),
        #     'conference_full_name': forms.TextInput(attrs={'class': 'konf'}),
        #     'conference_discription': forms.Textarea(attrs={'class': 'konf'}),
        #     'conference_date_start': forms.SelectDateWidget(attrs={'class': 'data'}),
        #     'conference_date_end':forms.SelectDateWidget(attrs={'class': 'data'}),
        #     'conference_date_reg_start': forms.SelectDateWidget(attrs={'class': 'data'}),
        #     'conference_date_reg_end': forms.SelectDateWidget(attrs={'class': 'data'}),
        #     'conference_format_id': forms.Select(attrs={'class': 'konf'}),
        #     'conference_faculty_id': forms.Select(attrs={'class': 'konf'}),
        #     'conference_building_id': forms.Select(attrs={'class': 'konf'}),
        }

class ExpertArticleUploadForm(ModelForm):
    class Meta:
        model=ExpertArticle
        fields= '__all__'
        widgets= {
            'expert':forms.HiddenInput(),
            'article':forms.FileInput(),
            'article_keywords':forms.Textarea(),
        }
