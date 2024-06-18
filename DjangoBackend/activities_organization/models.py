from django.db import models
import uuid
from login_and_register.models import CustomUser
from django.core.validators import MinValueValidator, MaxValueValidator


class CreateActivity(models.Model):
    activity_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    activity_name = models.TextField(max_length=30, default='UnnamedActivity')
    activity_level = models.IntegerField()  # 1,2,3
    activity_leader = models.ForeignKey(CustomUser, on_delete=models.CASCADE, to_field='personal_number')   # 活动创建人
    activity_guest = models.ManyToManyField(CustomUser, related_name='guest', blank=True, through='ActivityGuest')   # 嘉宾，可为空
    activity_participator = models.ManyToManyField(CustomUser, related_name='participator', blank=True, through='ActivityParticipator')  # 参与者
    activity_type = models.TextField(max_length=50)  # 活动类型
    activity_description = models.TextField(blank=True)  # 活动描述
    activity_budget = models.IntegerField()  # 预算   str(2000 - 400 - 800 = result)
    activity_condition = models.IntegerField(default=1)
    activity_place = models.CharField(max_length=20, default="")


class ActivityGuest(models.Model):
    activity = models.ForeignKey(CreateActivity, to_field='activity_id', on_delete=models.CASCADE)
    guest = models.ForeignKey(CustomUser, to_field='personal_number', on_delete=models.CASCADE)
    guest_condition = models.BooleanField(default=False)


class ActivityParticipator(models.Model):
    activity = models.ForeignKey(CreateActivity, to_field='activity_id', on_delete=models.CASCADE)
    participator = models.ForeignKey(CustomUser, to_field='personal_number', on_delete=models.CASCADE)
    p_condition = models.BooleanField(default=False)


# 时间的抽象类，无实体表
class AbstractTime(models.Model):
    start_time = models.CharField(max_length=30, null=True)  # 原始时间
    start_time_hours = models.IntegerField()  # 0-24h 依算法时间调整
    end_time = models.CharField(max_length=30, null=True)   # 原始时间
    end_time_hours = models.IntegerField()

    class Meta:
        abstract = True


# 提交的时间申请，与活动形成一对多关系
class TimeOption(AbstractTime):
    activity = models.ForeignKey(CreateActivity, on_delete=models.CASCADE, related_name='time_options', to_field='activity_id')
    option = models.CharField(max_length=50)    # a/b/c 用于区分是第几个备选项


# 最终确认的时间，与活动形成一对一关系,现有活动对象，创建活动时间时将活动加入
class ActivityTime(AbstractTime):
    activity = models.OneToOneField(CreateActivity, on_delete=models.CASCADE, related_name='activity_time', to_field='activity_id')


class Notice(models.Model):
    personal_number = models.CharField(max_length=9, editable=False, unique=False)
    activity_id = models.CharField(max_length=100, default="")
    title = models.TextField(max_length=100, default='Unnamed Notice')
    content = models.TextField(max_length=300)
    type = models.CharField(max_length=30, default='system')
    condition = models.BooleanField(default=True)
    activity_name = models.TextField(max_length=30, default='UnnamedActivity')


class Place(models.Model):
    place_name = models.CharField(max_length=100, unique=True)
    place_type = models.IntegerField(default=0, validators=[MinValueValidator(1), MaxValueValidator(3)])


class Cost(models.Model):
    activity = models.ForeignKey(CreateActivity, to_field='activity_id', on_delete=models.CASCADE)
    name = models.CharField(max_length=100,default='Unnamed')
    Type = models.CharField(max_length=30, default='none')
    description = models.TextField(max_length=300,default='none')
    cost_in = models.IntegerField(default=0)
    cost_out = models.IntegerField(default=0)
    rest = models.IntegerField(default=0)