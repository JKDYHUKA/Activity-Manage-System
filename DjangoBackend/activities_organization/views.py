from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from login_and_register.models import CustomUser
from .models import CreatActivity
import json


@csrf_exempt
def create_new_activity(request):
    if request.method == 'POST':
        activity_details = json.loads(request.body)
        activity_level = activity_details['activity_level']
        activity_leader = CustomUser.objects.get(username=activity_details['username'])
        activity_type = activity_details['activity_type']
        activity_description = activity_details['activity_description']
        activity_budget = activity_details['activity_budget']
        activity_guests = activity_details['activity_guests']
        activity_participators = activity_details['activity_participators']

        activity = CreatActivity.objects.create(activity_level=activity_level,
                                                activity_leader=activity_leader,
                                                activity_type=activity_type,
                                                activity_description=activity_description,
                                                activity_budget=activity_budget)

        if activity_guests != '':
            activity_guests = activity_guests.split(',')
            users = CustomUser.objects.filter(personal_number__in=activity_guests)
            for user in users:
                activity.activity_guest.add(user)

        if activity_participators != '':
            activity_participators = activity_participators.split(',')
            users = CustomUser.objects.filter(personal_number__in=activity_participators)
            for user in users:
                activity.activity_participator.add(user)

        activity.save()

        return JsonResponse({"message": "activity create successfully", "code": "0"}, status=200)


