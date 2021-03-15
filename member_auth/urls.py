from decimal import Context
from django.urls import path, reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('reg/', views.regPage, name="reg"),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('confirm/<uidb64>/<token>/', views.VerificationView, name="lkconfirm"),
    path('con/', views.lkconfirm, name="con"),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]
