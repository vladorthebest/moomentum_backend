from django.urls import path
from . import views


urlpatterns = [
    path('', views.ProfileAPI.as_view({'get': 'retrieve', 'put': 'update'})),
]