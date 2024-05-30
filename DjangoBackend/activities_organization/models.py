from django.db import models
import uuid
from login_and_register.models import CustomUser


class CreatActivity(models.Model):
    activity_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    activity_level = models.IntegerField()  # 1,2,3
    activity_leader = models.ForeignKey(CustomUser, on_delete=models.CASCADE)   # 活动创建人
    activity_guest = models.ManyToManyField(CustomUser, related_name='guest', blank=True)   # 嘉宾，可为空
    activity_participator = models.ManyToManyField(CustomUser, related_name='participator', blank=True)  # 参与者
    activity_type = models.TextField(max_length=50)  # 活动主题
    activity_description = models.TextField(blank=True) # 活动描述
    activity_budget = models.IntegerField()  # 预算
    activity_condition = models.BooleanField(default=False)


# 活动地点，与活动形成一对一关系
class Classroom(models.Model):
    classroom_id = models.CharField(max_length=3, editable=False, unique=True)
    name = models.CharField(max_length=50)
    activity = models.OneToOneField(CreatActivity, on_delete=models.CASCADE)


# 时间的抽象类，无实体表
class AbstractTime(models.Model):
    start_time_day = models.IntegerField()  # 1-7天
    start_time_hours = models.IntegerField()  # 0-24h 依算法时间调整
    end_time_day = models.IntegerField()
    end_time_hours = models.IntegerField()

    class Meta:
        abstract = True


# 提交的时间申请，与活动形成一对多关系
class TimeOption(AbstractTime):
    activity = models.ForeignKey(CreatActivity, on_delete=models.CASCADE)
    option = models.CharField(max_length=50)    # a/b/c 用于区分是第几个备选项


# 最终确认的时间，与活动形成一对一关系,现有活动对象，创建活动时间时将活动加入
class ActivityTime(AbstractTime):
    activity = models.OneToOneField(CreatActivity, on_delete=models.CASCADE)


class Notice(models.Model):
    personal_number = models.CharField(max_length=9, editable=False, unique=False, default="000000000")
    content = models.TextField(max_length=200)
    is_active = models.BooleanField(max_length=1)