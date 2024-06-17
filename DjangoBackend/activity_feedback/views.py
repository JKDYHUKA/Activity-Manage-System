from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
import jwt
import os
# import requests
from .models import *
from activities_organization.models import *
import redis
from asgiref.sync import async_to_sync
from channels.generic.websocket import AsyncWebsocketConsumer, WebsocketConsumer
from channels.exceptions import StopConsumer
# Create your views here.

@csrf_exempt
def subQuestionnaire(request):
    if request.method == 'POST':
        body = json.loads(request.body)
        role=body['usertype']
        satisfaction=body['rate']
        suggestion=body['suggestion']
        notice_id=body['notice_id']
        notice=Notice.objects.get(id=notice_id)
        notice_num=Notice.objects.filter(activity_id=notice.activity_id).count()
        # 人数
        Part_num=ActivityParticipator.objects.filter(activity_id=notice.activity_id).count()
        activity=CreateActivity.objects.get(activity_id=notice.activity_id)
        people_num=Part_num+ActivityGuest.objects.filter(activity=activity).count()+1
        #互动数
        Feedback.objects.create(
                role=role,
                satisfaction=satisfaction,
                suggestions=suggestion,
                activity_id=notice.activity_id,
            )
        data=ActivityData.objects.get(activity_id=notice.activity_id)
        data.people_num=people_num
        data.notice_num=notice_num
        data.save()
        return JsonResponse({"message": "feedback successfully", 'code': '0'},
                                status=200)

    else:
        return JsonResponse({"message": "method error"}, status=401)