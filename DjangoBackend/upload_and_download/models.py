from django.db import models
from django.utils import timezone


class FileInfo(models.Model):
    active_id = models.IntegerField(max_length=50)
    file_name = models.CharField(max_length=500)
    file_size = models.DecimalField(max_digits=10, decimal_places=0)
    file_path = models.CharField(max_length=500)
    upload_time = models.DateTimeField(default=timezone.now())