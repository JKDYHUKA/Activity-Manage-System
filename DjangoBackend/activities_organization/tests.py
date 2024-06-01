from django.test import TestCase
from django.urls import reverse


class TestYourAPIView(TestCase):
    def test_api_view(self):
        url = 'http://127.0.0.1:8000/api/api_test/'
        response = self.client.get(url)

        # 检查返回的状态码是否为200
        self.assertEqual(response.status_code, 200)
