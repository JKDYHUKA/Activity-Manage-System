

# Create your models here.
from django.db import models
import uuid
from django.core.validators import MinValueValidator, MaxValueValidator
# Create your models here.

class Feedback(models.Model):
    activity_id = models.UUIDField(default=uuid.uuid4, editable=False)
    role=models.CharField(max_length=255, blank=False, null=False)
    satisfaction=models.IntegerField(default=0,validators=[MinValueValidator(1),MaxValueValidator(5)])
    suggestions=models.TextField(default="")


class ActivityData(models.Model):
    activity_id = models.UUIDField(default=uuid.uuid4, editable=False,unique=True)
    people_num=models.IntegerField(default=0)
    chat_num=models.IntegerField(default=0)
    notice_num=models.IntegerField(default=0)