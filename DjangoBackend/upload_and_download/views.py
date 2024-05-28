from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.http import HttpResponseRedirect
from django.http import FileResponse
from django.template import RequestContext
from django.urls import reverse

# from django.utils.http import urlquote 由于版本更新（django4）将库替换成如下
from urllib.parse import quote

from .models import FileInfo
from .forms import UploadForm
import os


# 上传文件，存储到D:\\upload
def file_upload(request):
    # Handle file upload
    if request.method == 'POST':
        form = UploadForm(request.POST, request.FILES)
        if form.is_valid():
            files = request.FILES.getlist('file')
            # request里应包含活动id、文件名、文件大小
            for f in files:
                file_info = FileInfo(active_id=f.id, file_name=f.name, file_size=1 if 0 < f.size < 1024 else f.size / 1024,
                                     file_path=os.path.join('D:\\upload', f.name))
                file_info.save()
                # 上传
                destination = open(os.path.join("D:\\upload", f.name), 'wb+')
                for chunk in f.chunks():
                    destination.write(chunk)
                destination.close()

            # 返回上传页
            return HttpResponseRedirect('/uploader/list')
    else:
        form = UploadForm()  # A empty, unbound form
    # 未与前端连接，待修改
    return render(request, 'uploader/upload.html', {'form': form})


# 文件列表,需要传入该活动的id（actives_id），取出活动id与active_id匹配的项
def file_list(request,actives_id):
    file_infos = FileInfo.objects.get(active_id=actives_id)
    # 待修改
    return render(request, 'uploader/list.html', {'file_infos': file_infos})


# 下载文件
# 此处的id是fileinfo中为每个文件自动赋予的id
def file_download(request, id):
    file_info = FileInfo.objects.get(id=id)
    print('下载的文件名：' + file_info.file_name)
    file = open(file_info.file_path, 'rb')
    response = FileResponse(file)
    response['Content-Disposition'] = 'attachment;filename="%s"' % quote(file_info.file_name)
    return response


# 删除文件
def file_delete(request, id):
    file_info = FileInfo.objects.get(id=id)
    file_info.delete()
    file_infos = FileInfo.objects.all()

    return HttpResponseRedirect('/uploader/list')