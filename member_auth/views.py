from django.contrib.messages.api import error
from django.db.models.query import QuerySet
from django.forms.models import ModelForm, inlineformset_factory
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.conf import settings
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text, DjangoUnicodeDecodeError
from django.urls import reverse
from .utils import token_generator
from core.models import MemberApplication, MemberInfo, Conference
import datetime as DT
from django.views.generic.edit import CreateView, UpdateView
from django.contrib.auth import views as auth_views
from .forms import CreateuserForm



def regPage(request):

    form = CreateuserForm()
    if request.method == "POST":
        form = CreateuserForm(request.POST)

        if form.is_valid():
            form.save()
            user = form.cleaned_data.get("username")
            u = User.objects.get(username=user)
            u.is_active = False
            u.save()
            
            uidb64 = urlsafe_base64_encode(force_bytes(u.pk))

            domain = get_current_site(request).domain
            link = reverse('lkconfirm', kwargs={'uidb64': uidb64, 'token': token_generator.make_token(u)})
            activate_url='http://'+domain+link
            pochta=request.POST['email']
            email = EmailMessage(
                'АВТОРИЗАЦИЯ НА ПЛАТФОРМЕ ОГУ КОНФЕРЕНЦИИ',
                'Привет, ' + user + ', пожалуйста пройдите по ссылке для завершения ативации аккаунта\n' +
                activate_url + ' ссылка была отправлена на почту ' + pochta,
                settings.EMAIL_HOST_USER,
                [pochta]
            )
            email.fail_silently = False
            email.send()

            messages.success(request, "Учетная запись была создана для " + user)
            return redirect('con')
    context = {"form":form}
    return render(request, "registration/reg.html", context)


def VerificationView(self, uidb64, token):
    try:
        id = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=id)

        if not token_generator.check_token(user, token):
            return redirect('login'+'?message='+'User already activated')

        if user.is_active:
            return redirect('login')
        user.is_active = True
        user.save()

        messages.success(request, 'Account activated successfully')
        return redirect('login')

    except Exception as ex:
        pass
    return redirect('login')
 

def lkconfirm(request):
    return render(request, "registration/lkconfirm.html")






