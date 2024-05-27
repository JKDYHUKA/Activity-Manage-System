from datetime import datetime, timedelta
import jwt

from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, login, logout
from django.middleware.csrf import get_token
from .login_utils.login_utils import send_sms
from django.conf import settings
from .models import CustomUser
import json
import random

@csrf_exempt
def verify_token(request):
    if request.method == 'POST':
        header = request.headers
        authorization = header.get('Authorization')
        print(authorization)
        jwt_token = authorization.split(' ')[1]
        print(jwt_token)

        decoded_token = jwt.decode(jwt_token, settings.SECRET_KEY, algorithms=['HS256'])
        user = CustomUser.objects.get(username=decoded_token['username'])
        login(request, user)
        return JsonResponse({'message': 'login verify successfully', 'code': '0',
                             'username': user.username}, status=200)
    else:
        return JsonResponse({'message': 'failed'}, status=401)


@csrf_exempt
def verify(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        phone_number = data.get('phone_number')
        code_int = random.randint(100000, 999999)
        code = str(code_int)
        resp = send_sms(phone_number, code)
        print(resp)

        return JsonResponse({"code": code, "response": "成功发送验证码"}, status=200)
    else:
        return JsonResponse({'error': 'Only POST requests are allowed'}, status=405)


@csrf_exempt
def submit_register_form(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        print(data)
        user = CustomUser.objects.create_user(username=data['username'],
                                              email=data['email'],
                                              password=data['password'],
                                              phone_number=data['phone_number'])
        return JsonResponse({"message": "success"}, status=200)
        # if form.is_valid():
        #     form.save()
        #     return JsonResponse({"message": "success"}, status=200)
        #
        # else:
        #     return JsonResponse({'error': 'Property error '}, status=405)

    else:
        return JsonResponse({'error': 'Only POST requests are allowed'}, status=405)


@csrf_exempt
def user_login(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        username = data.get('username')
        password = data.get('password')
        print(username, password)

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            jwt_token = jwt.encode({'username': user.username}, settings.SECRET_KEY, algorithm='HS256')
            expiration_time = datetime.now() + timedelta(minutes=5)
            csrf_token = get_token(request)
            return JsonResponse({'login_code': '0',
                                 'message': 'login successfully',
                                 'jwt_token': jwt_token.decode(),
                                 'csrf_token': csrf_token,
                                 'expiration_time': expiration_time}, status=200)
        else:
            return JsonResponse({'login_code': '2'}, status=401)
    return JsonResponse({'message': 'Invalid request method'}, status=400)


@csrf_exempt
def reset_password(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        username = data.get('username')
        password = data.get('password')
        print("new password: ", password)

        try:
            user = CustomUser.objects.get(username=username)
        except CustomUser.DoesNotExist:
            return JsonResponse({"message": "username does not exist", "code": "1"}, status=404)

        user.set_password(password)
        user.save()

        logout(request)
        return JsonResponse({"message": "Password updated successfully", "code": "0"}, status=200)
    else:
        return JsonResponse({"message": "Wrong Method", "code": "1"}, status=405)

