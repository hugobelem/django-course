from django.urls import path

from . import views


urlpatterns = [
    path('', views.projects, name='projects'),
    path('project/<str:pk>/', views.project, name='project'),
    path('project/create', views.create_project, name='create'),
    path('project/update/<str:pk>/', views.update_project, name='update'),
    path('project/delete/<str:pk>/', views.delete_project, name='delete'),
]
