from django.test import TestCase
from .models import CustomUser as CU

def UserCreateTestCase(TestCase):

    def setUp(self):
        self.username = 'test1'
        self.email = 'test1@test.com'

    def test_create_user(self):
        old_count = CU.objects.count()
        CU.objects.create(username=self.username,
                          email=self.email)
        new_count = CU.objects.count()
        self.assertNotEqual(old_count, new_count)

