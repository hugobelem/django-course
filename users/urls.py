from django.urls import path

from . import views

urlpatterns = [
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.register_user, name='register'),
    path('account/', views.account_user, name='account'),

    path('', views.profiles, name='profiles'),
    path('profile/<str:pk>/', views.user_profile, name='user-profile'),
]
