from django.urls import path
from . import chat_utils

urlpatterns = [
    path('api/GetName/', chat_utils.GetName, name="GetName"),
]