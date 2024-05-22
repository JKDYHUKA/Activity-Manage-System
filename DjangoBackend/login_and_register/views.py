from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, login
from .forms import CustomUserCreationForm
from .login_utils.login_utils import send_sms
from .models import CustomUser
import json
import random


@csrf_exempt
def verify(request):
    if request.method == 'POST':
        print(request.POST)
        phone_number = request.POST.get('phone_number')
        code_int = random.randint(100000, 999999)
        code = str(code_int)
        resp = send_sms(phone_number, code)
        print(resp)

        return JsonResponse({"code": code})
    else:
        return JsonResponse({'error': 'Only POST requests are allowed'}, status=405)


@csrf_exempt
def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()

        else:
            return JsonResponse({'error': 'Property error '}, status=405)

    else:
        return JsonResponse({'error': 'Only POST requests are allowed'}, status=405)


@csrf_exempt
def user_login(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        username = data.get('username')
        password = data.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return JsonResponse({'message': 'Login successful'}, status=200)
        else:
            return JsonResponse({'message': 'Invalid login details provided'}, status=401)
    return JsonResponse({'message': 'Invalid request method'}, status=400)

