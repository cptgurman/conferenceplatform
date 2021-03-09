from django.forms import ModelForm, widgets
from django.contrib.auth.forms import  UserChangeForm, UserCreationForm
from django.contrib.auth.models import User
from django.forms.fields import DateField
from core.models import MemberInfo, Conference, MemberApplication
from django import forms
from django.forms.models import inlineformset_factory, modelform_factory, modelformset_factory



class OrderForm(ModelForm):
    class Meta:

        fields = "__all__"

class CreateuserForm(UserCreationForm):
    
    class Meta:
        model = User
        fields = ["username", "email", "password1", 'password2']


class lkUser(ModelForm):
    class Meta:
        model = MemberInfo
        fields = "__all__"
        widgets = {
        'memberinfo_dateofbirth': forms.SelectDateWidget,
        # 'memberinfo_user': forms.HiddenInput(),
        }
   
       


class MemberCreateApplication(ModelForm):
    class Meta:
        model = MemberApplication
        fields = "__all__"
        # widgets = {
        # 'member_name': forms.HiddenInput(),
        # 'member_application_status': forms.HiddenInput(),
        # 'member_application_comment': forms.HiddenInput(),
        # }


