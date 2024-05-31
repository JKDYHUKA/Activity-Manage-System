from django.db import models

# Create your models here.
from django.db import models
from django.utils import timezone
from activities_organization.models import CreatActivity


class FileInfo(models.Model):
    active = models.ForeignKey(CreatActivity, on_delete=models.CASCADE)
    file_name = models.CharField(max_length=500)
    file_size = models.DecimalField(max_digits=10, decimal_places=0)
    file_path = models.CharField(max_length=500)
    # upload_time = models.DateTimeField(default=timezone.now())