from django.shortcuts import render
from django.http import JsonResponse
from .forms import CustomUserCreationForm
from .login_utils.login_utils import send_sms
from .models import CustomUser
import json
import random


def verify(request):
    if request.method == 'POST':
        phone_number = request.POST.get('phone_number')
        code_int = random.randint(100000, 999999)
        code = str(code_int)
        resp = send_sms(phone_number, code)
        print(resp)

        return JsonResponse({"code": code})
    else:
        return JsonResponse({'error': 'Only POST requests are allowed'}, status=405)


def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()

        else:
            return JsonResponse({'error': 'Property error '}, status=405)

    else:
        return JsonResponse({'error': 'Only POST requests are allowed'}, status=405)

