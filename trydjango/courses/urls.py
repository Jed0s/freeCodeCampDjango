from django.urls import path

from . import views

app = 'courses'
urlpatterns = [
    path('', views.CourseListView.as_view(), name='courses_list_url'),
    path('<int:id>/', views.CourseView.as_view(), name='courses_detail_url'),
    path('create/', views.CourseCreateView.as_view(), name='course_create_url'),
    path('<int:id>/update', views.CourseUpdateView.as_view(), name='course_update.url'),
    path('<int:id>/delete', views.CourseDeleteView.as_view(), name='course_delete.url'),
]