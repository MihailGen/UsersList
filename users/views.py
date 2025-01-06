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


def home(request):
    return render(request, "users/home.html")


'''
def base(request):
    users = User.objects.all()
    return render(request, 'base.html', {'users': users})
'''


class SignUp(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "users/signup.html"


class MyTokenObtainPairView(TokenObtainPairView):
    permission_classes = (AllowAny,)


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer


class CustomView(APIView):
    permission_classes = [IsAuthenticated]


class MyModelViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = [CanEdit]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
