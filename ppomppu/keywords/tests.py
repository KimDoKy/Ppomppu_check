from django.test import TestCase
from .models import Keywords

from users.models import CustomUser as CU

class KeyWordsTestCase(TestCase):

    def setUp(self):
        self.keyword = 'test keyword'
        self.owner = CU.objects.create(name='tester1')
        self.test_instance = Keywords(keyword=self.keyword,
                                      owner=self.owner)

    def test_create_a_keyword(self):
        old_count = Keywords.objects.count()
        self.test_instance.save()
        new_count = Keywords.objects.count()
        self.assertNotEqual(old_count, new_count)
