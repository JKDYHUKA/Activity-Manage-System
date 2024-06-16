from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
import jwt
import os
import requests
from .models import Feedback
from activities_organization.models import Notice
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
        Feedback.objects.create(
                role=role,
                satisfaction=satisfaction,
                suggestions=suggestion,
                activity_id=notice.activity_id,
            )
        return JsonResponse({"message": "feedback successfully", 'code': '0'},
                                status=200)

    else:
        return JsonResponse({"message": "method error"}, status=401)