from django.urls import path
from . import views

urlpatterns = [
    path('api/subQuestionnaire/', views.subQuestionnaire, name="subQuestionnaire"),

]