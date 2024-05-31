from django.contrib import admin
from django.urls import path, include
from . import views

# app_name = 'uploader'

urlpatterns = [
     path('api/upload/', views.file_upload, name='upload'),  # 上传
    # path('list/', views.file_list),  # 列表
    # path('download/<id>', views.file_download, name='download'),  # 下载
    # path('delete/<id>', views.file_delete, name='delete'),  # 删除
]