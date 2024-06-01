from django.urls import path
from . import views

urlpatterns = [
    # path('api/create_new_activity/', )
    path('api/get_user_by_personal_number/', views.get_user_by_personal_number, name="get_user_by_personal_number"),
    path('api/create_new_activity/', views.create_new_activity, name="create new activity"),
    path('api/get_activities_by_personal_number/', views.get_activities_by_personal_number, name='get_activities_by_personal_number'),
    path('api/api_test/', views.api_algorithm_test, name='api_test'),
]