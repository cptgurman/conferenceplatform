from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required
from conf_member.views import MemberCreateApplicationView, MemberConfsList, MemberUpdateApplicationView, Search, ConferenceInfo, Recomendation, RecomendationList
from conf_member import views

urlpatterns = [
    path('member_data_update/<int:pk>', login_required(views.MemberDataUpdate.as_view(
        template_name='conf_member/MemberInfoUpdate.html')), name="MemberDataUpdate"),
    path('member_data_create/', login_required(views.MemberDataCreate.as_view(
        template_name='conf_member/MemberInfoCreate.html')), name="MemberDataCreate"),
    path('member_application_add/<int:conf_id>',
         login_required(MemberCreateApplicationView.as_view()), name='application_add'),
    path('member_application_update/<int:pk>',
         login_required(MemberUpdateApplicationView.as_view()), name='application_update'),
    path('member_lk/', login_required(MemberConfsList.as_view()),
         name='lk'),
    path('search/', Search.as_view(), name='search'),
    path('member_recommendation/', Recomendation.as_view(), name='recommendation'),
    path('member_recommendation_list/',
         RecomendationList.as_view(), name='recommendationlist'),
    path('conf_info/<int:conf_id>', ConferenceInfo.as_view(), name='conf_info'),
]
