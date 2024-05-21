from django.shortcuts import render
from django.http import JsonResponse
from django.utils import timezone


def get_current_time(request):
    current_time = timezone.now()
    return JsonResponse({'current_time': current_time})
