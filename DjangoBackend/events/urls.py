from django.urls import path
from . import views

urlpatterns = [
    path('get_current/', views.get_current_time, name='test'),
]
