from django.urls import path
from . import views
from conf_expert.views import ArticlesForReview, ExpertArticleReview, ExpertArticleUpload
from conf_expert import views

urlpatterns = [
    path('articles_for_review', ArticlesForReview.as_view(template_name='conf_expert/expert.html'), name="articles_for_review"),
    path('article_review/<int:pk>', ExpertArticleReview.as_view(template_name='conf_expert/reviewarcticle.html'), name='article_review'),
    path('expert_upload_articles/<int:pk>', ExpertArticleUpload.as_view(template_name='conf_expert/expert_upload_articles.html'), name='expert_upload_articles'),
    
]