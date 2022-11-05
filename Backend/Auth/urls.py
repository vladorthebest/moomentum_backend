from django.urls import path, include
from . import views


urlpatterns = [
    path('login/', views.LoginView.as_view()),
    path('ping/', views.PingView.as_view()),
]