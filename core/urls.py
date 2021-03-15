from django.urls import path
from core.views import HomePage


urlpatterns = [
    path('', HomePage.as_view(template_name = "base.html"), name='home'), 
]