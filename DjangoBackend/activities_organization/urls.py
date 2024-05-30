from django.urls import path
from . import views

urlpatterns = [
    # path('api/create_new_activity/', )
    path('api/get_user_by_personal_number/', views.get_user_by_personal_number, name="get_user_by_personal_number"),
]