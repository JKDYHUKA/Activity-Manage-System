from django.urls import path
from . import views

urlpatterns = [
    path('api/get_captcha/', views.verify, name='captcha'),
    path('api/submit_register_form/', views.submit_register_form, name='register'),
    path('api/login/', views.user_login, name='login'),
    path('api/reset_password/', views.reset_password, name='reset_password'),
    path('api/verify_token/', views.verify_token, name='verify_token'),
]
