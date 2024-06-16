from __future__ import absolute_import, unicode_literals
import os
from celery import Celery

# Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'DjangoBackend.settings')

app = Celery('DjangoBackend', broker='redis://127.0.0.1:6379/1', backend='redis://127.0.0.1:6379/2',
             timezone='Asia/Shanghai',
             imports='DjangoBackend.tasks'
             )

# 配置国际化
app.conf.timezone = 'Asia/Shanghai'
# 是否使用UTC
app.conf.enable_utc = False

# Load task modules from all registered Django app configs.
app.autodiscover_tasks()