from django.urls import path
from . import views

app_name = 'products'

urlpatterns = [
    path('', views.product_list_view, name='product_list_url'),
    path('create/', views.product_create_view, name='product_create_url'),
    path('<int:id>/', views.product_detail_view, name='product_detail_url'),
    path('<int:id>/update', views.product_update_view, name='product_update_url'),
    path('<int:id>/delete', views.product_delete_view, name='product_delete_url'),
]