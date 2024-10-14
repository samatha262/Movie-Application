from django.test import TestCase

# Create your tests here.
from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from .models import Collection
from django.contrib.auth.models import User

class MovieCollectionAPITests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.token = RefreshToken.for_user(self.user).access_token

    def test_register(self):
        response = self.client.post(reverse('register'), {'username': 'newuser', 'password': 'newpass'})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_list_movies(self):
        response = self.client.get(reverse('list_movies'), HTTP_AUTHORIZATION=f'Bearer {self.token}')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_collection(self):
        response = self.client.post(reverse('create_collection'), {'title': 'My Collection', 'description': 'My favorite movies'}, HTTP_AUTHORIZATION=f'Bearer {self.token}')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
