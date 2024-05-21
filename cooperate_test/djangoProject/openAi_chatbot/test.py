import openai
import requests
from djangoProject import settings
import base64
from PIL import Image
from io import BytesIO
import os

message = "Great! In that case, let's start with a general itinerary for a 10-day trip to Japan. \n\nDay 1: Arrive in Tokyo\n- Explore Tokyo and visit popular attractions such as the Tokyo Tower, Meiji Shrine, and Shibuya Crossing.\n- Enjoy authentic Japanese cuisine in local restaurants.\n\nDay 2: Tokyo\n- Visit the historic Asakusa district and explore Senso-ji Temple.\n- Take a cruise along the Sumida River.\n- Spend the evening in the vibrant nightlife areas of Shinjuku or Roppongi.\n\nDay 3: Day Trip to Nikko\n- Take a day trip to Nikko, known for its stunning temples and natural beauty.\n- Visit Toshogu Shrine, Nikko National Park, and Lake Chuzenji.\n- Return to Tokyo in the evening.\n\nDay 4: Kyoto\n- Travel to Kyoto by bullet train.\n- Explore Kinkaku-ji (Golden Pavilion), Nijo Castle, and Fushimi Inari Taisha Shrine.\n- Experience a traditional tea ceremony.\n\nDay 5: Kyoto\n- Visit the iconic Arashiyama Bamboo Grove.\n- Explore the beautiful gardens of Kiyomizu-dera Temple.\n- Discover the famous Geisha district, Gion.\n\nDay 6: Hiroshima and Miyajima Island\n- Take a day trip to Hiroshima and visit the Peace Memorial Park and Museum.\n- Take a ferry to Miyajima Island and see the famous floating Torii Gate.\n- Return to Kyoto in the evening.\n\nDay 7: Osaka\n- Travel to Osaka, known for its vibrant food scene and lively atmosphere.\n- Explore Osaka Castle, Dotonbori Street, and Shinsekai district.\n- Try local street food, such as takoyaki and okonomiyaki.\n\nDay 8: Nara\n- Take a day trip to Nara, home to friendly deer and ancient temples.\n- Visit Todai-ji Temple, Kasuga Shrine, and Nara Park.\n- Enjoy a traditional Japanese lunch in Nara.\n\nDay 9: Mount Fuji\n- Take a day trip to Mount Fuji, Japan's iconic volcano.\n- Visit the 5th Station for breathtaking views (weather permitting).\n- Take a cruise on Lake Ashi and ride the Hakone Ropeway for panoramic views.\n- Return to Tokyo in the evening.\n\nDay 10: Departure\n- Depending on your departure time, you may have some free time in Tokyo for shopping or last-minute sightseeing.\n- Depart from Tokyo.\n\nPlease note that this is just a suggested itinerary and can be customized based on your preferences and the specific time of your visit. Let me know if you have any specific locations or activities in mind, and I can further assist you in planning your trip to Japan!"


def test():
    openai_api_url = f"{settings.PROXY_API_URL}/v1/chat/completions"
    openai_api_image_url = f"{settings.PROXY_API_URL}/v1/images/generations"
    openai_api_edit_url = f"{settings.PROXY_API_URL}/v1/images/edits"
    headers = {
        'Authorization': '',
        'Content-Type': 'application/json',
    }
    data = {
        'model': 'gpt-3.5-turbo',
        'messages': [
            {'role': 'system', 'content': 'you should extract information from the following specific plan. your '
                                          'response is  like: Country: America City:'
                                          'New York, Day 1 morning: Statue of Liberty and Ellis Island, '
                                          'Day 1 afternoon: Battery Park. I mean you should only retain the time, '
                                          ' place names and city name, The shorter the better'},
            {'role': 'user', 'content': message}],
        'n': 1,
        'max_tokens': 800,
        'temperature': 0,
    }

    # response = requests.post(openai_api_url, json=data, headers=headers)
    # response_data = response.json()
    # result_message = response_data['choices'][0]['message']['content']
    # print(result_message)

    city_data = {
        'model': 'gpt-3.5-turbo',
        'messages': [
            {'role': 'system', 'content': 'you should extract information from the following specific plan. your '
                                          'response is  like: Tokyo, New York, Beijing. You only tell me the city names'},
            {'role': 'user', 'content': message}],
        'n': 1,
        'max_tokens': 800,
        'temperature': 0,
    }

    # city_response = requests.post(openai_api_url, json=city_data, headers=headers)
    # cities = city_response.json()
    # cities = cities['choices'][0]['message']['content']
    # print(cities)

    country_data = {
        'model': 'gpt-3.5-turbo',
        'messages': [
            {'role': 'system', 'content': 'you should extract information from the following specific plan. your '
                                          'response is  like: America, China. You only tell me the country names'},
            {'role': 'user', 'content': message}],
        'n': 1,
        'max_tokens': 800,
        'temperature': 0,
    }

    # country_response = requests.post(openai_api_url, json=country_data, headers=headers)
    # countries = country_response.json()
    # countries = countries['choices'][0]['message']['content']
    # print(countries)

    image_data = {
        'prompt': "A map of the China only with black lines. Additionally, the continent is white and the picture only contain the mentioned country",
        'n': 2,
        'size': "1024x1024",
        'response_format': 'b64_json',
    }

    # image_response = requests.post(openai_api_image_url, json=image_data, headers=headers)
    # im_res = image_response.json()
    # b64_encoded_image = im_res['data'][0]['b64_json']
    #
    # # 将Base64编码的图片数据解码为字节数据
    # image_data = base64.b64decode(b64_encoded_image)
    #
    # # 使用PIL将字节数据转换回图片对象
    # image = Image.open(BytesIO(image_data))
    # image.show()
    #
    # # 保存图片到本地（可选）
    # image.save("output_image.png")

    # with open('C://Users//JKDYHUKA//Desktop//img-kdRKxto1Z1n1FvbeKAVeK7CV.png', 'rb') as image_file:
    #     image_data = base64.b64encode(image_file.read()).decode('utf-8')
    #     edit_headers = {
    #         'Authorization': '',
    #         'Content-Type': 'multipart/form-data',
    #     }
    #
    #     edit_data = {
    #         'image': image_file,
    #         "prompt": "mark Beijing in this Map of China",
    #         "n": 2,
    #         "size": "1024x1024"
    #     }
    #
    #     edit_response = requests.post(openai_api_edit_url, edit_data, headers=edit_headers, files={'image': image_file})
    #     edit_result = edit_response.content
    #     print(edit_result)

    image_path = 'C://Users//JKDYHUKA//Desktop//img-kdRKxto1Z1n1FvbeKAVeK7CV.png'
    # image = Image.open(image_path)
    #
    # # 将图片转换为RGBA格式, 要不然openai会报错
    # image_rgba = image.convert('RGBA')
    # image_rgba.save('C://Users//JKDYHUKA//Desktop//img-convert.png')

    # curl_command = 'curl -X POST https://service-7ocrpmdk-1319570416.hk.apigw.tencentcs.com/v1/images/edits ' \
    #                '-H "Authorization: " ' \
    #                '-F image="@C://Users//JKDYHUKA//Desktop//img-convert.png" ' \
    #                '-F prompt="change" ' \
    #                '-F n=2 ' \
    #                '-F size="1024x1024"'
    # os.system(curl_command)

    image = Image.open("C://Users//JKDYHUKA//Desktop//qhzz.png")
    image.resize((1024, 1024))
    image.save("C://Users//JKDYHUKA//Desktop//qhzz-convert.png")
    curl_command_0 = 'curl -X POST https://service-7ocrpmdk-1319570416.hk.apigw.tencentcs.com/v1/images/variations ' \
                     '-H "Authorization: " ' \
                     '-F image="@C://Users//JKDYHUKA//Desktop//qhzz-convert.png" ' \
                     '-F n=5 ' \
                     '-F size="1024x1024"'
    os.system(curl_command_0)


if __name__ == '__main__':
    test()
