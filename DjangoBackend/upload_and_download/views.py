import json
import os
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.http import HttpResponse
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile



@csrf_exempt
def file_upload(request):
    if request.method == 'POST':
        # 处理文件上传

        if 'file' in request.FILES:
            file = request.FILES['file']
            # 自定义文件存储路径
            act_id = request.POST.get('act_id')
            file_name = f"{act_id}_{file.name}"

            custom_path = os.path.join(os.getenv('FILE_STORAGE_PATH'), file_name)
            file_name = default_storage.save(custom_path, ContentFile(file.read()))

            return JsonResponse({"message": "file received", "file_name": file_name}, status=200)
        else:
            return JsonResponse({"message": "No file uploaded"}, status=400)
    else:
        return JsonResponse({"message": "Invalid request method"}, status=405)


@csrf_exempt
def get_filename(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        act_id = data['act_id']['act_id']
        base_path = os.getenv("BASED_PATH")

        file_name = []
        for root, dirs, files in os.walk(base_path):
            for file in files:
                split_file_name = file[37:]
                file_flag = file[:36]
                if act_id == file_flag:
                    file_name.append(split_file_name)

        return JsonResponse({"message": "get file name successfully", "filenamelist": file_name}, status=200)


def download_file(request, act_id, file_name):
    file_path = os.path.join(os.getenv("BASED_PATH"), f"{act_id}_{file_name}")
    if os.path.exists(file_path):
        with open(file_path, 'rb') as fh:
            response = HttpResponse(fh.read(), content_type="application/octet-stream")
            response['Content-Disposition'] = 'inline; filename=' + os.path.basename(file_path)
            return response
    else:
        return HttpResponse("文件未找到", status=404)
