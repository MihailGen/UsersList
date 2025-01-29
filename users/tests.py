from django.test import TestCase
from django.urls import reverse
from rest_framework import status


from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse
from rest_framework.test import APITestCase
from django.contrib.auth.models import User

from django.contrib.auth import get_user_model
User = get_user_model()

class AuthenticatedAPITests(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass', email='test@mail.ru')
        self.client.login(username='testuser', password='testpass', email='test@mail.ru')

    def test_authenticated_access(self):
        url = reverse('register')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)  # Доступ разрешен для аутентифицированного пользователя

    def test_signup(self):
        url = reverse('signup')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)  # Доступ разрешен для аутентифицированного пользователя

    def test_api_register(self):
        url = reverse('register')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)  # Доступ разрешен для аутентифицированного пользователя

    def test_home(self):
        url = reverse('home')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)  # Доступ разрешен для аутентифицированного пользователя