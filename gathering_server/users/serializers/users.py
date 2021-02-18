# Django rest framework imports
from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from gathering_server.users.models import User


class UserModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'username',
            'email'
        ]


class SignUpSerializer(serializers.Serializer):

    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=User.objects.all())]
    )

    username = serializers.CharField(
        min_length=3,
        max_length=20,
        required=True,
        validators=[UniqueValidator(queryset=User.objects.all())]
    )

    password = serializers.CharField(min_length=8, max_length=256, required=True)
    password_confirmation = serializers.CharField(min_length=8, max_length=256, required=True)

    def validate(self, data):
        if data['password'] != data['password_confirmation']:
            raise serializers.ValidationError('password don\'t match')
        return data

    def create(self, data):
        data.pop('password_confirmation')
        user = User.objects.create_user(
            email=data['email'],
            username=data['username'],
            password=data['password'],
        )
        return UserModelSerializer(user).data
