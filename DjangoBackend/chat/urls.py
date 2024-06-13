from django.urls import path
from . import chat_utils

urlpatterns = [
    path('api/GetName/', chat_utils.GetName, name="GetName"),
    path('api/GetGuests/', chat_utils.GetGuests, name="GetGuests"),
    path('api/GetLeader/', chat_utils.GetLeader, name="GetLeader"),
]