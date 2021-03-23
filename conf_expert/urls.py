from django.urls import path
from . import views
from conf_expert.views import ArticlesForReview
from conf_expert import views

urlpatterns = [
    path('articles_for_review', ArticlesForReview.as_view(template_name='conf_expert/expert.html'), name="articles_for_review"),
]