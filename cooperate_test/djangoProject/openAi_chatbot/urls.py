from django.urls import path
from . import views

urlpatterns = [
    path('', views.AgentChatGPT, name='ChatGPT'),
    path('travel_chatbot/', views.travel_chatbot, name='TravelChatBot'),
    path('travel_chatbot/generalise/', views.generalise, name='generalise'),
    path('api/get_message', views.ask_openai_api, name='get_message'),
    path('api/register', views.register, name='register'),
    path('api/getHistoryMessage', views.AgentChatGPT, name='History'),
    path('api/travel_chatbot', views.travel_chatbot, name='getTravelChatBot'),
    path('api/deleteMessagesByType', views.deleteMessagesByType, name='deleteMessagesByType'),

]
