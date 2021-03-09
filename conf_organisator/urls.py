from django.urls import path
from django.contrib.auth.decorators import login_required, permission_required
from conf_organisator.views import ConferenceUpdate, ConferenceCreate, ConferenceListView


urlpatterns = [
    
    path('createconf/', ConferenceCreate.as_view(template_name='conf_organisator/createconf.html'), name="create_conf"),
    path('updateconf/<int:pk>', ConferenceUpdate.as_view(template_name='conf_organisator/updateconf.html'), name="edit_conf"),
    path('myconf/', ConferenceListView.as_view(template_name = "myconfs.html"), name="myconf"),

]
