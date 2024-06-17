from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from login_and_register.models import CustomUser
from .models import CreateActivity, TimeOption, ActivityGuest, ActivityParticipator, Notice
from django.conf import settings
from .activity_utils.organization_utils import get_number, calculate_hours_difference_from_tomorrow_midnight, \
    list_to_tuple_with_processing, activities_manage, decode_jwt_token, generate_activity_details, con_detect, \
    generate_created_activities_details, create_system_invitation_notices
import json
import jwt
import os

from datetime import datetime, timedelta
from celery.result import AsyncResult

from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from django_celery_beat.models import PeriodicTask, IntervalSchedule
from DjangoBackend.tasks import modify_notice_condition
from DjangoBackend.celery import app

from dotenv import load_dotenv
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Load environment variables from .env file
load_dotenv(os.path.join(BASE_DIR, '.env'))


@csrf_exempt
def create_new_activity(request):
    if request.method == 'POST':
        header = request.headers
        decoded_token = decode_jwt_token(header)
        leader_user = CustomUser.objects.get(username=decoded_token['username'])

        activity_details = json.loads(request.body)
        activity_name = activity_details['name']
        activity_level = activity_details['activity_level']
        activity_level = get_number(activity_level)
        if activity_level == -1:
            return JsonResponse({"message": 'activity_level error'}, status=500)
        activity_leader = leader_user
        activity_type = activity_details['activity_type']
        activity_description = activity_details['activity_describe']
        activity_budget = activity_details['activity_budget']

        time1 = activity_details['time1']['_rawValue']
        time2 = activity_details['time2']['_rawValue']
        time3 = activity_details['time3']['_rawValue']

        processed_time1 = list_to_tuple_with_processing(
            [calculate_hours_difference_from_tomorrow_midnight(date) for date in time1])
        processed_time2 = list_to_tuple_with_processing(
            [calculate_hours_difference_from_tomorrow_midnight(date) for date in time2])
        processed_time3 = list_to_tuple_with_processing(
            [calculate_hours_difference_from_tomorrow_midnight(date) for date in time3])
        
        if con_detect(processed_time1, processed_time2, processed_time3, leader_user) == -1:
            return JsonResponse({"message": 'time conflict error'}, status=500)

        userid_str = activity_details['userid_str']
        usertype_str = activity_details['usertype_str']

        activity = CreateActivity.objects.create(activity_level=activity_level,
                                                 activity_leader=activity_leader,
                                                 activity_type=activity_type,
                                                 activity_description=activity_description,
                                                 activity_budget=activity_budget,
                                                 activity_name=activity_name, )

        notice_list = create_system_invitation_notices(activity, userid_str, usertype_str)

        Notice.objects.bulk_create(notice_list)

        # 第一志愿
        TimeOption.objects.create(start_time=time1[0],
                                  start_time_hours=processed_time1[0],
                                  end_time=time1[1],
                                  end_time_hours=processed_time1[1],
                                  activity=activity,
                                  option='a')

        # 第二志愿
        TimeOption.objects.create(start_time=time2[0],
                                  start_time_hours=processed_time2[0],
                                  end_time=time2[1],
                                  end_time_hours=processed_time2[1],
                                  activity=activity,
                                  option='b')

        # 第三志愿
        TimeOption.objects.create(start_time=time3[0],
                                  start_time_hours=processed_time3[0],
                                  end_time=time3[1],
                                  end_time_hours=processed_time3[1],
                                  activity=activity,
                                  option='c')

        return JsonResponse({"message": "activity create successfully", "code": "0"}, status=200)


@csrf_exempt
def get_user_by_personal_number(request):
    if request.method == 'POST':
        body = json.loads(request.body)
        personal_number = body['userId']

        try:
            user = CustomUser.objects.get(personal_number=personal_number)
            return JsonResponse({"message": "add user successfully", 'code': '0', "username": user.username},
                                status=200)
        except CustomUser.DoesNotExist:
            return JsonResponse({"message": "user does not exit", "code": "1"}, status=200)

    else:
        return JsonResponse({"message": "method error"}, status=401)


def get_activities_by_personal_number(request):
    if request.method == 'GET':
        header = request.headers
        decoded_token = decode_jwt_token(header)
        leader = CustomUser.objects.get(username=decoded_token['username'])
        created_activities = CreateActivity.objects.filter(activity_leader_id=leader.personal_number)
        guest_activities = CreateActivity.objects.filter(activity_guest=leader, activityguest__guest_condition=1)
        participator_activities = CreateActivity.objects.filter(activity_participator=leader,
                                                                activityparticipator__p_condition=1)

        user_activities = guest_activities | participator_activities
        guest_p_act_details = generate_activity_details(user_activities)
        created_act_details = generate_created_activities_details(created_activities)

        act_details = created_act_details + guest_p_act_details
        print(act_details)

        return JsonResponse({"message": "ok", "code": "0", "act_details": act_details}, status=200)


@csrf_exempt
def accept_invitation(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        notice_id = data['id']
        notice_content = str(data['content'])
        personal_number = data["userid"]
        notice = Notice.objects.get(id=notice_id)
        notice.title = "accepted"
        notice.save()

        notice_role = 'unknown'
        if notice_content.endswith('嘉宾'):
            notice_role = 'guest'
        elif notice_content.endswith('参与者'):
            notice_role = 'participator'


        # 根据角色选择要修改的模型
        if notice_role == 'guest':
            activity_guest_model = ActivityGuest
            activity_guest = activity_guest_model.objects.get(activity_id=notice.activity_id, guest_id=personal_number)
            activity_guest.guest_condition = True  # 修改条件字段为 True
            activity_guest.save()
        elif notice_role == 'participator':
            activity_p_model = ActivityParticipator
            activity_guest = activity_p_model.objects.get(activity_id=notice.activity_id, guest_id=personal_number)
            activity_guest.p_condition = True  # 修改条件字段为 True
            activity_guest.save()
        else:
            return JsonResponse({'message': 'Invalid role'}, status=400)

        return JsonResponse({"message": "condition update successfully", "code": "0"}, status=200)


@csrf_exempt
def refuse_invitation(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        notice_id = data['id']
        notice = Notice.objects.get(id=notice_id)
        notice.title = 'refused'
        notice.save()

        return JsonResponse({"message": "condition update successfully", "code": "0"}, status=200)


# need to be modified
@csrf_exempt
def activity_member_modify(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        act_id = data['act_id']
        userid_str = data['userid_str']
        usertype_str = data['usertype_str']

        activity = CreateActivity.objects.get(activity_id=act_id)

        notice_list = create_system_invitation_notices(activity, userid_str, usertype_str)
        Notice.objects.bulk_create(notice_list)
        return JsonResponse({"message": "Added member successfully", "code": "0"}, status=200)


@csrf_exempt
def get_all_members(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        act_id = data['act_id']
        activity = CreateActivity.objects.get(activity_id=act_id)
        if activity.activity_condition > 1:
            guests = ActivityGuest.objects.filter(activity=activity, guest_condition=True)
            participators = ActivityParticipator.objects.filter(activity=activity, p_condition=True)
        else:
            guests = ActivityGuest.objects.filter(activity=activity)
            participators = ActivityParticipator.objects.filter(activity=activity)

        guest_details = []
        for guest in guests:
            guest_details.append({
                "username": guest.guest.username,
                "userid": guest.guest.personal_number,
                "usertype": "嘉宾",
            })

        participator_details = []
        for p in participators:
            participator_details.append({
                "username": p.participator.username,
                "userid": p.participator.personal_number,
                "usertype": "参会人员",
            })

        act_members = guest_details + participator_details

        return JsonResponse({"message": "successfully", "code": "0", "tableData": act_members}, status=200)


def get_notices(request):
    if request.method == 'GET':
        header = request.headers
        decoded_token = decode_jwt_token(header)
        user = CustomUser.objects.get(username=decoded_token['username'])
        activities = CreateActivity.objects.all()
        # 创建一个字典来存储activity_id和对应的activity_type
        activity_dict = {}
        for activity in activities:
            act_str = str(activity.activity_id)
            activity_dict[act_str] = activity.activity_type

        notices = Notice.objects.filter(personal_number=user.personal_number, condition=True)
        notices_details = []
        for notice in notices:
            # print("type",notice.activity_id)
            if notice.activity_id in activity_dict:
                act_type = activity_dict[notice.activity_id]

            notices_details.append({
                "notice_id": notice.id,
                "act_name": notice.activity_name,
                "notice_content": notice.content,
                "notice_type": notice.type,
                "notice_title": notice.title,
                "act_type": act_type
            })

        return JsonResponse({"message": "get notices successfully", "code": "0", "notice_details": notices_details}, status=200)


@csrf_exempt
def create_notice_by_user(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        act_id = data['act_id']
        notice_content = data['notice_content']
        notice_title = data['notice_title']

        activity = CreateActivity.objects.get(activity_id=act_id)
        guests = ActivityGuest.objects.filter(activity=activity, guest_condition=True)
        participators = ActivityParticipator.objects.filter(activity=activity, p_condition=True)

        notice_list = []
        for guest in guests:
            notice = Notice(personal_number=guest.guest.personal_number,
                            activity_id=act_id,
                            title=notice_title,
                            content=notice_content,
                            type='user',
                            activity_name=activity.activity_name)
            notice_list.append(notice)

        for p in participators:
            notice = Notice(personal_number=p.participator.personal_number,
                            activity_id=act_id,
                            title=notice_title,
                            content=notice_content,
                            type='user',
                            activity_name=activity.activity_name)
            notice_list.append(notice)

        Notice.objects.bulk_create(notice_list)
        return JsonResponse({"message": "create notices successfully", "code": '0'}, status=200)


@csrf_exempt
def get_notice_number(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        act_id = data['act_id']
        act_condition = data['act_condition']

        result = {}
        if act_condition == '待定':
            result['accept_number'] = 0
            result['send_number'] = 0
        else:
            notices_list = Notice.objects.filter(activity_id=act_id)
            result['send_number'] = len(notices_list)
            accept = 0
            for n in notices_list:
                if n.title != 'Invitation':
                    accept += 1
            result['accept_number'] = accept

        return JsonResponse({"message": "get notice number successfully", "code": "0", "number": result}, status=200)

@csrf_exempt
def activity_finish(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        act_step = data['act_step']
        act_id = data['act_id']

        activity = CreateActivity.objects.get(activity_id=act_id)

        activity.activity_condition = act_step
        activity.save()

    return JsonResponse({"message": "activity finish", "code": "0"}, status=200)


@csrf_exempt
def set_reminder(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        t = data['time']['_rawValue']
        content = data['notice_content']
        pn = data['userid']

        time_delay = timedelta(seconds=30)
        t_time = datetime.now()
        eta = time_delay + t_time

        notice = Notice.objects.create(personal_number=pn,
                                       activity_id='0000000000000000000',
                                       title='提醒',
                                       content=content,
                                       type='user',
                                       condition=False,
                                       activity_name='reminder')

        res = modify_notice_condition.apply_async(args=[notice.id], countdown=10)
        return JsonResponse({"message": "successfully!!!!!!!"}, status=200)


def api_algorithm_test(request):
    if request.method == 'GET':
        activities_manage()
        return JsonResponse({"message": "test"}, status=200)

