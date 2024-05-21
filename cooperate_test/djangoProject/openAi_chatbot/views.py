import os
from io import BytesIO

from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse, Http404
import base64
from PIL import Image
from djangoProject import settings
import requests
from . import models
import json

# openai image edi end point
# https://api.openai.com/v1/images/edits
#

openai_api_key = 'qiangsang_simida'
Authorization = ''


def ask_openai(message, model_type):
    # message = transform(message)
    print(message)
    message_stored = models.Message(sequence_id=1, message=message, role='user', model_type=model_type)
    message_stored.save()

    # something here to contribute message
    message_array = getAllSortedMessageByModelType(model_type)
    print(message_array)

    openai_api_url = f"{settings.PROXY_API_URL}/v1/chat/completions"
    headers = {
        'Authorization': '',
        'Content-Type': 'application/json',
    }
    data = {
        'model': 'gpt-3.5-turbo',
        'messages': message_array,
        'max_tokens': 2000,
        'n': 1,
        'temperature': 0.8,
    }

    # data['messages'].append(message_object)

    try:
        response = requests.post(openai_api_url, json=data, headers=headers)
        response_data = response.json()
        if 'error' in response_data:
            result_message = response_data['error']['message']
            print(result_message)
            return result_message

        result_message = response_data['choices'][0]['message']['content']
        role = response_data['choices'][0]['message']['role']
        # result_message = transform(result_message)
        print(result_message)
        response_stored = models.Message(sequence_id=1, message=result_message, role=role, model_type=model_type)
        response_stored.save()
        return result_message
    except requests.exceptions.RequestException as e:
        print(e)
        return 'some was wrong'


def getAllSortedMessageById():
    messages_array = []
    try:
        messages = models.Message.objects.filter(sequence_id=1).order_by('id')
        for message in messages:
            dic = {
                "role": message.role,
                "content": message.message,
            }
            messages_array.append(dic)
    except models.Message.DoesNotExist:
        print('no messages found')
    return messages_array


def getAllSortedMessageByModelType(model_type):
    messages_array = []
    try:
        messages = models.Message.objects.filter(model_type=model_type).order_by('id')
        for message in messages:
            dic = {
                "role": message.role,
                "content": message.message,
            }
            messages_array.append(dic)
    except models.Message.DoesNotExist:
        print('no messages found')
    return messages_array


def get_country_name():
    set_generalise_role = {'role': 'system',
                           'content': 'you should extract countries from the following '
                                      'specific plan when I say extract. you should only retain the country names'
                                      ' The shorter the better. your'
                                      'response is  like: America, China'}
    set_command = {'role': 'user', 'content': 'extract'}
    message_array = getAllSortedMessageByModelType('travel_chatbot')
    message_array = message_array[1:]
    message_array.insert(0, set_generalise_role)
    message_array.append(set_command)


    openai_api_url = f"{settings.PROXY_API_URL}/v1/chat/completions"
    headers = {
        'Authorization': Authorization,
        'Content-Type': 'application/json',
    }

    generalise_data = {
        'model': 'gpt-3.5-turbo',
        'messages': message_array,
        'n': 1,
        'max_tokens': 800,
        'temperature': 0,
    }

    country_response = requests.post(url=openai_api_url, json=generalise_data, headers=headers)
    country_data = country_response.json()
    country = country_data['choices'][0]['message']['content']
    return country


def get_created_image(country, image_name: str):
    prompt = "A map of " + country + " only with black lines. Additionally, the continent is white and the picture only contain the mentioned country"
    openai_api_image_url = f"{settings.PROXY_API_URL}/v1/images/generations"
    headers = {
        'Authorization': '',
        'Content-Type': 'application/json',
    }
    image_data = {
        'prompt': prompt,
        'n': 2,
        'size': "512x512",
        'response_format': 'b64_json',
    }

    image_response = requests.post(openai_api_image_url, json=image_data, headers=headers)
    im_res = image_response.json()
    b64_encoded_image = im_res['data'][0]['b64_json']

    # 将Base64编码的图片数据解码为字节数据
    image_data = base64.b64decode(b64_encoded_image)

    # 使用PIL将字节数据转换回图片对象
    image = Image.open(BytesIO(image_data))

    path = 'D://Users//JKDYHUKA//PycharmProjects//djangoProject//openAi_chatbot//static//image'
    image_name = image_name + '.png'
    completed_path = os.path.join(path, image_name)
    # 保存图片到本地（可选）
    image.save(completed_path)
    print("image created successfully")
    return image_name

@csrf_exempt
def travel_chatbot(request):
    if request.method == 'POST':
        message_info = json.loads(request.body)
        message = message_info.get('message')
        print("travel_message: ", message)
        response = ask_openai(message, 'travel_chatbot')
        return JsonResponse({'response': response})

    # initialize the chatbot
    role_message = {'role': 'system',
                    'content': 'You are a travel information assistant. Only answer questions related to travel. '
                               'Additionally, you should list the specific plan regarding to specific time and '
                               'location after you get access to those information. You must show me the specific attractions The specific time is not the '
                               'specific date but like this: the first day morning'}
    welcome_message = {'role': 'assistant',
                       'content': 'Hello, I am your travel assistant, you can tell me your ideas and I will give your '
                                  'a travel plan'}
    messages_array = getAllSortedMessageByModelType("travel_chatbot")
    if len(messages_array) == 0:
        role_stored = models.Message(sequence_id=1, role=role_message['role'], message=role_message['content'],
                                     model_type='travel_chatbot')
        role_stored.save()
        welcome_stored = models.Message(sequence_id=1, role=welcome_message['role'], message=welcome_message['content'],
                                        model_type='travel_chatbot')
        welcome_stored.save()

        messages_array.append(role_message)
        messages_array.append(welcome_message)

    # messages_array = json.dumps(messages_array)
    # print(messages_array)
    return JsonResponse({'message': messages_array[1:]})


def AgentChatGPT(request):
    if request.method == 'POST':
        message = request.POST.get('message')
        response = ask_openai(message, 'gpt-3.5-turbo')
        return JsonResponse({'response': response})

    # 从数据库中获取历史信息
    messages_array = getAllSortedMessageByModelType("gpt-3.5-turbo")
    # messages_array = json.dumps(messages_array)
    return JsonResponse({'message': messages_array})


def generalise(request):
    set_generalise_role = {'role': 'system',
                           'content': 'you should extract final information from the following '
                                      'specific plan when I say extract. you should only retain all the day time, '
                                      'city name, country name and the attractions, The shorter the better. your'
                                      'response is  like: Country: America City:'
                                      'New York, Day 1 morning: Statue of Liberty and Ellis Island, '
                                      'Day 1 afternoon: Battery Park. '}
    set_command = {'role': 'user', 'content': 'extract'}
    message_array = getAllSortedMessageByModelType('travel_chatbot')
    message_array = message_array[1:]
    message_array.insert(0, set_generalise_role)
    message_array.append(set_command)
    print(message_array)

    openai_api_url = f"{settings.PROXY_API_URL}/v1/chat/completions"
    headers = {
        'Authorization': Authorization,
        'Content-Type': 'application/json',
    }

    generalise_data = {
        'model': 'gpt-3.5-turbo',
        'messages': message_array,
        'n': 1,
        'max_tokens': 800,
        'temperature': 0,
    }

    generalise_response = requests.post(url=openai_api_url, json=generalise_data, headers=headers)
    g_data = generalise_response.json()
    g_data = g_data['choices'][0]['message']['content']

    country_name = get_country_name()
    print(country_name)

    image_name = get_created_image('America', 'America')

    result_data = {'content': g_data}
    return render(request=request, template_name='generalise.html', context={'result': result_data, 'image_name': image_name})


@csrf_exempt
def ask_openai_api(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            message = data.get('message')
            response = ask_openai(message, 'gpt-3.5-turbo')
            return JsonResponse({'success': True, 'response': response})
        except json.JSONDecodeError:
            return JsonResponse({'success': False, 'message': 'Invalid JSON data in the request body.'})


def register(request):
    if request.method == 'POST':
        try:
            user_info = json.loads(request.body)
            userName = user_info.get('userName')
        except json.JSONDecodeError:
            return JsonResponse({'success': False, 'message': 'invalid JSON data in the request body'})

@csrf_exempt
def deleteMessagesByType(request):
    if request.method == 'POST':
        try:
            model_info = json.loads(request.body)
            model_type = model_info.get('model_type')
            print(model_type)

            messages_deleted, _ = models.Message.objects.filter(model_type=model_type).delete()

            if messages_deleted > 0:
                print("success")
                return JsonResponse({'success': True, 'message': 'Messages deleted successfully'})
            else:
                return JsonResponse({'success': False, 'message': 'No matching messages found'})
        except Exception as e:
            print('Error:', e)
            return JsonResponse({'success': False, 'message': 'An error occurred while deleting messages'})
