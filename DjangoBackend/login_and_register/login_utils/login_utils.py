import hashlib

from aliyunsdkcore.client import AcsClient
from aliyunsdkcore.request import CommonRequest
from dotenv import load_dotenv
from pathlib import Path
import os
import random
from ..models import CustomUser

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Load environment variables from .env file
load_dotenv(os.path.join(BASE_DIR, '.env'))


def send_sms(phone, code):
    ACCESS_KEY_ID = os.getenv("ALIYUN_ACCESS_ID")
    ACCESS_KEY_SECRET = os.getenv("ALIYUN_ACCESS_SECRET")

    # 创建AcsClient实例，用于发送请求到阿里云服务，参数包括AccessKey ID和Secret，以及服务区域（这里是杭州）
    client = AcsClient(ACCESS_KEY_ID, ACCESS_KEY_SECRET, 'cn-hangzhou')

    request = CommonRequest()
    request.set_accept_format('json')
    request.set_domain('dysmsapi.aliyuncs.com')
    request.set_method('POST')
    request.set_protocol_type('https')
    request.set_version('2017-05-25')
    request.set_action_name('SendSms')

    request.add_query_param('RegionId', "cn-hangzhou")
    request.add_query_param('PhoneNumbers', phone)
    request.add_query_param('SignName', "ustb")
    request.add_query_param('TemplateCode', "SMS_461880248")
    request.add_query_param('TemplateParam', '{"code": "%s"}' % code)

    # 发送请求，并获取响应
    response = client.do_action_with_exception(request)
    return response


def generate_unique_id(username):
    # 将用户名转换为UTF-8编码的字节串
    username_bytes = username.encode('utf-8')
    # 使用SHA-256哈希算法计算哈希值
    hash_object = hashlib.sha256(username_bytes)
    # 获取哈希值的十六进制表示
    hex_digest = hash_object.hexdigest()
    # 将十六进制表示的哈希值转换为整数
    hash_integer = int(hex_digest, 16)
    # 截取前8位作为独特的8位数字
    unique_id = hash_integer % 100000000  # 10^8
    return '4' + str(unique_id)

