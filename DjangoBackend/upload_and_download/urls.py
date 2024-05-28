from django.contrib import admin
from django.urls import path, include
from . import views

app_name = 'uploader'

urlpatterns = [
    path('', views.upload, name='upload'),  # 上传
    path('list/', views.list),  # 列表
    path('download/<id>', views.download, name='download'),  # 下载
    path('delete/<id>', views.delete, name='delete'),  # 删除
]