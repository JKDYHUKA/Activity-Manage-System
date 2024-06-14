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

from django.core.files.storage import default_storage
from django.core.files.base import ContentFile

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

        return JsonResponse({"message": "ok", "code": "0", "act_details": act_details}, status=200)


def get_notice(request):
    if request.method == 'GET':
        header = request.headers
        decoded_token = decode_jwt_token(header)
        user = CustomUser.objects.get(username=decoded_token['username'])
        notices = Notice.objects.filter(personal_number=user.personal_number, condition=1)

        notice_detail = []
        for notice in notices:
            detail = {
                "notice_content": notice.content,
                "notice_title": notice.title,
                "notice_id": notice.id,
            }
            notice_detail.append(detail)

        return JsonResponse({"message": "get notice successfully", "code": "0", "notices": notice_detail}, status=200)


@csrf_exempt
def accept_invitation(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        notice_id = data['id']
        notice_role = data['role']
        personal_number = data["userid"]
        notice = Notice.objects.get(id=notice_id)
        notice.title = "accepted"
        notice.save()

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
        guests = activity.activity_guest.all()
        participators = activity.activity_participator.all()

        guest_details = []
        for guest in guests:
            guest_details.append({
                "username": guest.username,
                "userid": guest.personal_number,
                "usertype": "嘉宾",
            })

        participator_details = []
        for p in participators:
            participator_details.append({
                "username": p.username,
                "userid": p.personal_number,
                "usertype": "参会人员",
            })

        act_members = guest_details + participator_details

        return JsonResponse({"message": "successfully", "code": "0", "tableData": act_members}, status=200)


def get_notices(request):
    if request.method == 'GET':
        header = request.headers
        decoded_token = decode_jwt_token(header)
        user = CustomUser.objects.get(username=decoded_token['username'])

        notices = Notice.objects.filter(personal_number=user.personal_number, condition=True)
        notices_details = []
        for notice in notices:

            notices_details.append({
                "act_name": notice.activity_name,
                "notice_content": notice.content,
                "notice_type": notice.type,
                "notice_title": notice.title,
            })

        return JsonResponse({"message": "get notices successfully", "code": "0", "notice_details": notices_details}, status=200)


def api_algorithm_test(request):
    if request.method == 'GET':
        activities_manage()
        return JsonResponse({"message": "test"}, status=200)

# @csrf_exempt
# def api_test(request):
#     if request.method == 'POST':
#         # 处理文件上传
#         if 'file' in request.FILES:
#             file = request.FILES['file']
#             # 自定义文件存储路径
#             custom_path = os.path.join(os.getenv('FILE_STORAGE_PATH'), file.name)
#             file_name = default_storage.save(custom_path, ContentFile(file.read()))
#
#             # 这里可以添加对文件的进一步处理逻辑，例如存储文件路径或进行文件分析
#             print(f"File saved path: {custom_path}")
#
#             return JsonResponse({"message": "file received", "file_name": file_name}, status=200)
#         else:
#             return JsonResponse({"message": "No file uploaded"}, status=400)
#     else:
#         return JsonResponse({"message": "Invalid request method"}, status=405)
