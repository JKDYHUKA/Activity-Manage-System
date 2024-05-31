from django.shortcuts import render

# Create your views here.
import re

from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.http import FileResponse
from django.template import RequestContext
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
#from .forms import UploadForm
# from django.utils.http import urlquote 由于版本更新（django4）将库替换成如下
from urllib.parse import quote

from .models import FileInfo
# from .forms import UploadForm
import os


@csrf_exempt
def file_upload(request):
    if request.method == 'POST' and request.FILES.get('file'):
        files = request.FILES.getlist('file')
        for f in files:
            # file_info = FileInfo(active_id=f.id, file_name=f.name, file_size=1 if 0 < f.size < 1024 else f.size / 1024,
            #                                           file_path=os.path.join('D:\\upload', f.name))
            file_info = FileInfo( file_name=f.name, file_size=1 if 0 < f.size < 1024 else f.size / 1024,
                                 file_path=os.path.join('D:\\upload', f.name))
            file_info.save()
            destination = open(os.path.join("D:\\upload", f.name), 'wb+')
            for chunk in f.chunks():
                destination.write(chunk)
            destination.close()
        return JsonResponse({'message': 'File uploaded successfully'})
    else:
        return JsonResponse({'error': 'No file uploaded'}, status=400)