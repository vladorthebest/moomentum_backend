from django.urls import path
from . import views

urlpatterns = [
    path('', views.LevelAPI.as_view({'get':'retrieve'})),
]
