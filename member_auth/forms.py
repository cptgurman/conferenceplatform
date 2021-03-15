from django.forms import ModelForm, widgets
from django.contrib.auth.forms import  UserChangeForm, UserCreationForm
from django.contrib.auth.models import User


class CreateuserForm(UserCreationForm):
    
    class Meta:
        model = User
        fields = ["username", "email", "password1", 'password2']




