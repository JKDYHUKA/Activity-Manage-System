from aliyunsdkcore.client import AcsClient
from aliyunsdkcore.request import CommonRequest
from dotenv import load_dotenv
from pathlib import Path
import os

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
    request.add_query_param('SignName', "yaolegouProject")
    request.add_query_param('TemplateCode', "SMS_461880248")
    request.add_query_param('TemplateParam', '{"code": "%s"}' % code)

    # 发送请求，并获取响应
    response = client.do_action_with_exception(request)
    return response
