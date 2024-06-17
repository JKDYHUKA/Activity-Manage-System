from django.urls import path
from . import views

urlpatterns = [
    path('api/subQuestionnaire/', views.subQuestionnaire, name="subQuestionnaire"),
    path('api/generate_report/', views.generate_report, name='generate report')
]
