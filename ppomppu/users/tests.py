from django.test import TestCase

from rest_framework.test import APIClient
from rest_framework.authtoken.models import Token
from .models import CustomUser as CU

class UserCreateTestCase(TestCase):

    def setUp(self):
        self.username = 'test'
        self.email = 'test@test.com'
        self.password = 'test123'

        user = CU.objects.create_user(username=self.username,
                                      email=self.email,
                                      password=self.password)
        user.save()

        self.client = APIClient()

        self.test_username = 'test1'
        self.test_email = 'test1@test.com'
        self.test_password = 'test1234'

    def test_create_user(self):
        old_count = CU.objects.count()
        CU.objects.create_user(username=self.test_username,
                               email=self.test_email,
                               password=self.test_password)
        new_count = CU.objects.count()
        self.assertNotEqual(old_count, new_count)

    def test_api_login_user(self):
        data = {'username': self.username,
                'email': self.email,
                'password': self.password}
        res = self.client.post('/rest-auth/login/', data)
        self.assertEqual(res.status_code, 200)

    def test_api_logout(self):
        data = {'username': self.username,
                'email': self.email,
                'password': self.password}
        res = self.client.post('/rest-auth/login/', data)
        access_token = Token.objects.get()
        print(access_token)
        access_token = 'Bearer ' + str(access_token)}
        res = self.client.post('/rest-auth/logout/', HTTP_AUTHORIZATION=access_token)
        print('result token: ', Token.objects.all())
        self.assertEqual(res.status_code, 200)

