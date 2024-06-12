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

from django.core.files.storage import default_storage
from django.core.files.base import ContentFile

from dotenv import load_dotenv
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Load environment variables from .env file
load_dotenv(os.path.join(BASE_DIR, '.env'))


@csrf_exempt
def GetName(request):
    if request.method == 'POST':
        body = json.loads(request.body)
        personal_number = body['userId']
        try:
            user = CustomUser.objects.get(personal_number=personal_number)
            return JsonResponse({"message": "get user successfully", 'code': '0', "username": user.username},
                                status=200)
        except CustomUser.DoesNotExist:
            return JsonResponse({"message": "user does not exit", "code": "1"}, status=200)

    else:
        return JsonResponse({"message": "method error"}, status=401)
