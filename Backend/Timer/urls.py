from django.urls import path
from . import views

urlpatterns = [
    path('create/', 
        views.ActivityViewSet.as_view({'get':'retrieve', 'post':'create'}), 
        name="timer_button"
    ),

]
