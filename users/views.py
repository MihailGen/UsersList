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

from datetime import time

# ----------------- Prometheus encapsulate --------------------------

from fastapi import FastAPI, Request
from prometheus_client import Counter, Histogram, generate_latest, CONTENT_TYPE_LATEST
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.responses import Response

app = FastAPI()

REQUEST_COUNT = Counter('request_count', 'Total number of requests', ['UsersList', 'endpoint'])
REQUEST_LATENCY = Histogram('request_latency_seconds', 'Request latency', ['UsersList', 'endpoint'])


class MetricsMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        endpoint = request.url.path
        REQUEST_COUNT.labels(app_name='UsersList', endpoint=endpoint).inc()
        with REQUEST_LATENCY.labels(app_name='UsersList', endpoint=endpoint).time():
            response = await call_next(request)
        return response


app.add_middleware(MetricsMiddleware)


@app.get('/metrics')
async def metrics():
    data = generate_latest()
    return Response(content=data, media_type=CONTENT_TYPE_LATEST)


@app.get('/compute')
def compute():
    time.sleep(2)
    return {"message": "Completed a complex computation"}


@app.get('/heavy_compute')
def heavy_compute():
    for t in range(150):
        time.sleep(2)
    return {"message": "Completed a series of computations"}


# --------------- Prometheus End ---------------------------------




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
