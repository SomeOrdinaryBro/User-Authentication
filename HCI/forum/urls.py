from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name="homepage"),
    path('register/', views.register, name="register"),
    path('login/', views.login, name="login"),
    path('dashboard/', views.dashboard, name="dashboard"),
    path('user-logout/', views.user_logout, name="user-logout"),
    path('weather-app/', views.weather_app, name="weather-app"),
]
