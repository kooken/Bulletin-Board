from djoser.serializers import UserCreateSerializer as BaseUserRegistrationSerializer
from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()



class UserRegistrationSerializer(BaseUserRegistrationSerializer):
    """ Сериализатор для регистрации """
    class Meta(BaseUserRegistrationSerializer.Meta):
        fields = ('email', 'first_name', 'last_name', 'password', 'phone', 'image')


class CurrentUserSerializer(serializers.ModelSerializer):
    """ Сериализатор для просмотра текущего пользователя """
    class Meta(BaseUserRegistrationSerializer.Meta):
        model = User
        fields = ('first_name', 'last_name', 'phone', 'image')
