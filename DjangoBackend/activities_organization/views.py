from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from login_and_register.models import CustomUser
from .models import CreatActivity
from django.conf import settings
from .activity_utils.organization_utils import get_number, calculate_hours_difference_from_tomorrow_midnight
import json
import jwt


@csrf_exempt
def create_new_activity(request):
    if request.method == 'POST':
        header = request.headers
        authorization = header.get('Authorization')
        jwt_token = authorization.split(' ')[1]

        decoded_token = jwt.decode(jwt_token, settings.SECRET_KEY, algorithms=['HS256'])
        leader_user = CustomUser.objects.get(username=decoded_token['username'])

        activity_details = json.loads(request.body)
        activity_name = activity_details['name']
        activity_level = activity_details['activity_level']
        activity_level = get_number(activity_level)
        if activity_level == -1:
            return JsonResponse({"message": 'activity_level error'}, status=500)
        activity_leader = leader_user
        activity_type = activity_details['activity_type']
        activity_description = activity_details['activity_describe']
        activity_budget = activity_details['activity_budget']

        time1 = activity_details['time1']
        time2 = activity_details['time2']['_rawValue']
        time3 = activity_details['time3']

        processed_time1 = [calculate_hours_difference_from_tomorrow_midnight(date) for date in time1]
        processed_time2 = [calculate_hours_difference_from_tomorrow_midnight(date) for date in time2]
        processed_time3 = [calculate_hours_difference_from_tomorrow_midnight(date) for date in time3]

        userid_str = activity_details['userid_str']
        usertype_str = activity_details['usertype_str']
        print(processed_time2)

        activity = CreatActivity.objects.create(activity_level=activity_level,
                                                activity_leader=activity_leader,
                                                activity_type=activity_type,
                                                activity_description=activity_description,
                                                activity_budget=activity_budget,
                                                activity_name=activity_name,)

        guest = [id for id, category in zip(userid_str, usertype_str) if category == '嘉宾']
        participants = [id for id, category in zip(userid_str, usertype_str) if category == '参会人员']

        if len(guest) != 0:
            users = CustomUser.objects.filter(personal_number__in=guest)
            for user in users:
                activity.activity_guest.add(user)

        if len(participants) != 0:
            users = CustomUser.objects.filter(personal_number__in=participants)
            for user in users:
                activity.activity_participator.add(user)

        # activity.save()

        return JsonResponse({"message": "activity create successfully", "code": "0"}, status=200)


@csrf_exempt
def get_user_by_personal_number(request):
    if request.method == 'POST':
        body = json.loads(request.body)
        personal_number = body['userId']

        try:
            user = CustomUser.objects.get(personal_number=personal_number)
            return JsonResponse({"message": "add user successfully", 'code': '0', "username": user.username}, status=200)
        except CustomUser.DoesNotExist:
            return JsonResponse({"message": "user does not exit", "code": "1"}, status=200)

    else:
        return JsonResponse({"message": "method error"}, status=401)

