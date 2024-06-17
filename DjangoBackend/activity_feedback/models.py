from django.db import models
import uuid
from django.core.validators import MinValueValidator, MaxValueValidator


class Feedback(models.Model):
    activity_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    role = models.CharField(max_length=255, blank=False, null=False)
    satisfaction = models.IntegerField(default=0, validators=[MinValueValidator(1), MaxValueValidator(5)])
    suggestions = models.TextField(default="")
