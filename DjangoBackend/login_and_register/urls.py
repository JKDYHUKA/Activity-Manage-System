from django.urls import path
from . import views

urlpatterns = [
    path('api/get_captcha/', views.verify, name='captcha'),
    path('api/submit_register_form', views.register, name='register')
]
