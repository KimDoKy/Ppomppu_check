from django.test import TestCase
from django.urls import reverse

from rest_framework.test import APIClient
from rest_framework import status

from .models import Post
from users.models import CustomUser

class ModelTestCase(TestCase):

    def setUp(self):
        user = CustomUser(email="tester999@test.com")
        user.save()
        self.post_title = "test title"
        self.post = Post(title=self.post_title, author=user)

    def test_model_can_create_a_post(self):
        old_count = Post.objects.count()
        self.post.save()
        new_count = Post.objects.count()
        self.assertNotEqual(old_count, new_count)


class ViewTestCase(TestCase):

    def setUp(self):
        user = CustomUser(email="tester999@test.com")
        user.save()
        self.user = user
        self.client = APIClient()
        self.client.force_authenticate(user=user)
        self.post_data = {
            'title':'test title',
            'author': user.id
            }
        self.response = self.client.post(
            reverse('create'),
            self.post_data,
            format='json')

    def test_api_can_create_a_post(self):
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)

    def test_api_can_get_a_post(self):
        post = Post.objects.get()
        response = self.client.get(
                reverse('detail', kwargs={'pk':post.id}),
                format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, post)

    def test_api_can_update_a_post(self):
        post = Post.objects.get()
        change_data = {'title':'change title', 'author':self.user.id}
        res = self.client.put(
                reverse('detail', kwargs={'pk':post.id}),
                change_data, format='json')
        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_api_can_a_delete_post(self):
        post = Post.objects.get()
        response = self.client.delete(
                reverse('detail', kwargs={'pk':post.id}),
                format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
