from django.urls import path
from . import views

urlpatterns = [
    path('', views.CreateActivity.as_view(), name="start_timer")
]
