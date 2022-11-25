from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.CreateActivity.as_view(), name="start_timer"),
    path('check/', views.CheckActivity.as_view(), name="check_timer"),
]
