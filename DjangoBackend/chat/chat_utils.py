from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from login_and_register.models import CustomUser
from activities_organization.models import CreateActivity, TimeOption, ActivityGuest, ActivityParticipator, Notice
from django.conf import settings
from activities_organization.activity_utils.organization_utils import get_number, calculate_hours_difference_from_tomorrow_midnight, \
    list_to_tuple_with_processing, activities_manage, decode_jwt_token, generate_activity_details,con_detect
import json
import jwt
import os
import requests

from django.core.files.storage import default_storage
from django.core.files.base import ContentFile

from dotenv import load_dotenv
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Load environment variables from .env file
load_dotenv(os.path.join(BASE_DIR, '.env'))

PROXY_API_URL='https://service-7ocrpmdk-1319570416.hk.apigw.tencentcs.com'

@csrf_exempt
def GetName(request):
    if request.method == 'POST':
        body = json.loads(request.body)
        personal_number = body['userId']
        try:
            user = CustomUser.objects.get(personal_number=personal_number)
            print(user.username)
            return JsonResponse({"message": "get user successfully", 'code': '0', "username": user.username},
                                status=200)
        except CustomUser.DoesNotExist:
            return JsonResponse({"message": "user does not exit", "code": "1"}, status=200)

    else:
        return JsonResponse({"message": "method error"}, status=401)

@csrf_exempt
def GetGuests(request):
    if request.method == 'POST':
        body = json.loads(request.body)
        personal_number = body['userId']
        activity_id = body['activityId']
        try:
            user = ActivityGuest.objects.filter(guest=personal_number, activity_id=activity_id)
            if user.exists():
                return JsonResponse({"message": "is guests", 'code': '0'},
                                    status=200)
            else:
                return JsonResponse({"message": "not guests", 'code': '2'},
                                    status=200)
        except CustomUser.DoesNotExist:
            return JsonResponse({"message": "user does not exit", "code": "1"}, status=200)

    else:
        return JsonResponse({"message": "method error"}, status=401)


@csrf_exempt
def GetLeader(request):
    if request.method == 'POST':
        body = json.loads(request.body)
        activity_id = body['activityId']
        print(activity_id)
        try:
            activity = CreateActivity.objects.get(activity_id=activity_id)
            print(activity.activity_leader)
            return JsonResponse({"message": "get leader successfully", 'code': '0', "userid": activity.activity_leader.personal_number},
                                status=200)
        except CustomUser.DoesNotExist:
            return JsonResponse({"message": "user does not exit", "code": "1"}, status=200)

    else:
        return JsonResponse({"message": "method error"}, status=401)


def ask_openai(context):
    print("---------------------------------asking------------------------------------")

    openai_api_url = f"{PROXY_API_URL}/v1/chat/completions"
    api_key = os.getenv('OPENAI_API_KEY')
    headers = {
        'Authorization': f"Bearer {api_key}",
        'Content-Type': 'application/json',
    }
    data = {
        'model': 'gpt-3.5-turbo',
        'messages': context,
        'max_tokens': 2000,
        'n': 1,
        'temperature': 0.8,
    }
    try:
        response = requests.post(openai_api_url, json=data, headers=headers)
        response_data = response.json()
        if 'error' in response_data:
            result_message = response_data['error']['message']
            print(result_message)
            return result_message

        result_message = response_data['choices'][0]['message']['content']
        role = response_data['choices'][0]['message']['role']

        return result_message
    except requests.exceptions.RequestException as e:
        print(e)
        return 'some was wrong'
