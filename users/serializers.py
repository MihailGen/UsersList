from rest_framework import serializers
from .models import User


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    def create(self, validated_data):
        logger.info('Работа со списком пользователей')
        user = User.objects.create_user(
            username=validated_data['email'],
            phone=validated_data['phone'],
            password=validated_data['password'],
        )
        return user

    class Meta:
        model = User
        fields = ('email', 'phone', 'password')