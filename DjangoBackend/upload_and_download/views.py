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

from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from .models import FileInfo
# from .forms import UploadForm
import os


@csrf_exempt
def file_upload(request):
    if request.method == 'POST':
        # 处理文件上传
        if 'file' in request.FILES:
            file = request.FILES['file']
            # 自定义文件存储路径
            custom_path = os.path.join(os.getenv('FILE_STORAGE_PATH'), file.name)
            file_name = default_storage.save(custom_path, ContentFile(file.read()))

            # 这里可以添加对文件的进一步处理逻辑，例如存储文件路径或进行文件分析
            print(f"File saved path: {custom_path}")

            return JsonResponse({"message": "file received", "file_name": file_name}, status=200)
        else:
            return JsonResponse({"message": "No file uploaded"}, status=400)
    else:
        return JsonResponse({"message": "Invalid request method"}, status=405)