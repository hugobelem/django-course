from django.urls import path

from . import views


urlpatterns = [
    path('', views.projects, name='projects'),
    path('<str:pk>/', views.project, name='project'),
    path('create', views.create_project, name='create'),
    path('update/<str:pk>/', views.update_project, name='update'),
    path('delete/<str:pk>/', views.delete_project, name='delete'),
]

