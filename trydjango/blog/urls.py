from django.urls import path
from . import views

app_name = 'articles'

urlpatterns = [
    path('', views.ArticleListView.as_view(), name='article_list_url'),
    path('<int:id>/', views.ArticleDetailView.as_view(), name='article_detail_url'),
    path('create/', views.ArticleCreateView.as_view(), name='article_create_url'),
    path('<int:id>/update', views.ArticleUpdateView.as_view(), name='article_update_url'),
    path('<int:id>/delete', views.ArticleDeleteView.as_view(), name='article_delete_url'),
]