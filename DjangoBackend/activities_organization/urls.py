from django.urls import path
from . import views

urlpatterns = [
    # path('api/create_new_activity/', )
    path('api/get_user_by_personal_number/', views.get_user_by_personal_number, name="get_user_by_personal_number"),
    path('api/create_new_activity/', views.create_new_activity, name="create new activity"),
    path('api/get_activities_by_personal_number/', views.get_activities_by_personal_number, name='get_activities_by_personal_number'),
    path('api/accept_invitation/', views.accept_invitation, name='accept invitation'),
    path('api/refuse_invitation/', views.refuse_invitation, name='refuse invitation'),
    path('api/activity_member_modify/', views.activity_member_modify, name='activity_member_modify'),
    path('api/get_all_members/', views.get_all_members, name='get all members'),
    path('api/get_notices/', views.get_notices, name='get notices'),
    path('api/create_notice/', views.create_notice_by_user, name='create notice'),
    path('api/get_notice_number/', views.get_notice_number, name='get notice number'),
    path('api/set_reminder/', views.set_reminder, name='set remainder'),
    path('api/api_test/', views.api_algorithm_test, name='api_test'),
    path('api/activity_finish/', views.activity_finish, name='activity_finish'),
]