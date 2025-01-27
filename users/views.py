import logging

from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from rest_framework import generics
from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework_simplejwt.views import TokenObtainPairView

from .models import User
from .permissions import CanEdit
from .serializers import RegisterSerializer

logging.config.fileConfig('config.ini')
logger = logging.getLogger(__name__)


def home(request):
    logger.debug("Отладка из функции создания домашней странички")
    logger.info('Вход пользователя ' + request.user.username + ' на домашнюю страничку')
    try:
        return render(request, "users/home.html")
    except Exception as e:
        logger.error(f"Произошла ошибка создания домашней страницы {e}")


'''
# Прежняя домашняя страничка приложения
def base(request):
    users = User.objects.all()
    return render(request, 'base.html', {'users': users})
'''


class SignUp(CreateView):
    logger.debug("Отладка из представления SignUp")
    logger.info('Создание странички аутентификация пользователя')
    try:
        form_class = UserCreationForm
        success_url = reverse_lazy("login")
        template_name = "users/signup.html"
    except Exception as e:
        logger.error(f"Произошла ошибка создания страницы аутентификации {e}")


class MyTokenObtainPairView(TokenObtainPairView):
    logger.debug("Отладка из MyTokenObtainPairView")
    logger.info('Работа с токенами')
    try:
        permission_classes = (AllowAny,)
    except Exception as e:
        logger.error(f"Произошла ошибка прав аутентификации {e}")


class RegisterView(generics.CreateAPIView):
    logger.debug("Отладка из представления RegisterView")
    logger.info('Работа со списком пользователей')
    try:
        queryset = User.objects.all()
        permission_classes = (AllowAny,)
        serializer_class = RegisterSerializer
    except Exception as e:
        logger.error(f"Произошла ошибка: {e}")


class CustomView(APIView):
    logger.debug("Отладка из CustomView")
    logger.info('Работа со списком пользователей')
    try:
        permission_classes = [IsAuthenticated]
    except Exception as e:
        logger.error(f"Произошла ошибка прав аутентификации: {e}")


class MyModelViewSet(viewsets.ModelViewSet):
    logger.debug("Отладка из MyModelViewSet")
    logger.info('Работа со списком пользователей')
    try:
        queryset = User.objects.all()
        serializer_class = RegisterSerializer
    except Exception as e:
        logger.error(f"Произошла ошибка: {e}")
    permission_classes = [CanEdit]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
