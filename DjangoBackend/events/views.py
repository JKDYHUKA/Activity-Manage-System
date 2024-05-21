from django.shortcuts import render
from django.http import JsonResponse
from django.utils import timezone


def get_current_time(request):
    current_time = timezone.now()
    year = str(current_time.year)
    month = str(current_time.month)
    day = str(current_time.day)
    return JsonResponse({'year': year, 'month': month, 'day': day})

