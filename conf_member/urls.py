from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required
from conf_member.views import lk, MemberCreateApplicationView
from conf_member import views

urlpatterns = [
    path('member_lk/', lk.as_view(template_name='conf_member/lk.html'), name="lk"),
    path('member_data_update/<int:pk>', login_required(views.MemberDataUpdate.as_view(template_name='conf_member/MemberInfoUpdate.html')), name="MemberDataUpdate"),
    path('member_data_create/', login_required(views.MemberDataCreate.as_view(template_name='conf_member/MemberInfoCreate.html')), name="MemberDataCreate"),
    path('member_application_add/<int:conf_id>',login_required(MemberCreateApplicationView.as_view()), name='application_add'), 
]