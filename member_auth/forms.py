from django.forms import ModelForm, widgets
from django.contrib.auth.forms import  UserChangeForm, UserCreationForm
from django.contrib.auth.models import User
from django import forms


class CreateuserForm(UserCreationForm):
    password1 = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(attrs={'class':'password1', 'type':'password', 'align':'center', 'placeholder':'Пароль'}),
    )
    password2 = forms.CharField(
        label="Confirm password",
        widget=forms.PasswordInput(attrs={'class':'password2', 'type':'password', 'align':'center', 'placeholder':'Повторите пароль'}),
    )
    class Meta:
        model = User
        fields = ["username", "email"]
        widgets = {
            'username': forms.TextInput(attrs={'class': 'username', "placeholder": "Логин"}),
            'email': forms.EmailInput(attrs={'class': 'email', "placeholder": "Почта"}),
        }


