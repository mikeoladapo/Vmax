from rest_framework import serializers
from .models import CustomUser , VideoFile
from django.core.validators import RegexValidator
from django.contrib.auth.hashers import make_password

username_regex = RegexValidator(
    regex=r'^[a-zA-Z0-9_]+$',
    message="Username must be alphanumeric or contain underscores."
)

class CustomUserSerializer(serializers.Serializer):
    username = serializers.CharField(
        max_length=20,
        validators=[username_regex],  
        error_messages={"unique": "username is already taken"}
    )
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)
    is_active = serializers.BooleanField(default=True,read_only=True)
    is_staff = serializers.BooleanField(default=True,read_only=True)
    is_superuser = serializers.BooleanField(default=False,read_only=True)
    def create(self, validated_data):
        password = validated_data.pop("password")
        validated_data["pasword"] = make_password(password)
        return CustomUser.objects.create(**validated_data)
    def update(self, instance, validated_data):
        instance.username = validated_data.get("username",instance.username)
        instance.email = validated_data.get("email",instance.email)
        password = validated_data.get("password")
        if password:
            instance.password = make_password(password)
            instance.save()
    def validate_username(self, value):
        if CustomUser.objects.filter(username=value).exists():
            raise serializers.ValidationError("username already taken")
        return value

class VideoFileSerializer(serializers.ModelSerializer):
    class Meta : 
        model = VideoFile
        fields = "_all_"
