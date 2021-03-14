from decimal import Context
from django.urls import path
from django.contrib.auth.decorators import login_required
from django.contrib.auth import views as auth_views
from . import views
from member_auth.views import lk, MemberCreateApplicationView, HomePage
from member_auth import views

urlpatterns = [
    path('', HomePage.as_view(template_name = "base.html"), name='home'),
    path('reg/', views.regPage, name="reg"),
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('lk/', lk.as_view(template_name='registration/lk.html'), name="lk"),
    path('confirm/<uidb64>/<token>/', views.VerificationView, name="lkconfirm"),
    path('con/', views.lkconfirm, name="con"),
    path('MemberDataUpdate/<int:pk>', login_required(views.MemberDataUpdate.as_view(template_name='registration/MemberInfoUpdate.html')), name="MemberDataUpdate"),
    path('MemberDataCreate/', login_required(views.MemberDataCreate.as_view(template_name='registration/MemberInfoCreate.html')), name="MemberDataCreate"),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('application/<int:pk>', MemberCreateApplicationView.as_view(), name='memberapplication'), 
    
    
]
