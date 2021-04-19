from django.forms import ModelForm, widgets
from core.models import MemberApplication, ExpertArticle
from django import forms



class ExpertReview(ModelForm):
    class Meta:
        model = MemberApplication
        fields = ['app_status', 'expert_app_comment']
        widgets = {
             
            'app_status': forms.Select(attrs={'class': 'Review'}),
            'expert_app_comment': forms.Textarea(attrs={'class': 'Review'}),

        }

class ExpertArticleUploadForm(ModelForm):
    class Meta:
        model=ExpertArticle
        fields= '__all__'
        widgets= {
            'expert':forms.HiddenInput(),
            'article':forms.FileInput(attrs={'class': 'ExpertArticle'}),
            'article_keywords':forms.Textarea(attrs={'class': 'ExpertArticle'}),
        }
