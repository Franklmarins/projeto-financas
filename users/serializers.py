from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from .models import User


class UserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        validators=[
            UniqueValidator(
                queryset=User.objects.all(), message="Email already exists!"
            )
        ]
    )
    username = serializers.CharField(
        validators=[
            UniqueValidator(
                queryset=User.objects.all(), message="username already exists!"
            )
        ]
    )
    password = serializers.CharField(write_only=True)
    is_superuser = serializers.BooleanField(default=False, write_only=True)

    def create(self, validated_data: dict) -> User:
        return User.objects.create_user(**validated_data)

    def update(self, instance: User, validated_data: dict) -> User:
        password = validated_data.pop("password", None)
        for key, value in validated_data.items():
            setattr(instance, key, value)

            if password:
                instance.set_password(password)

        instance.save()

        return instance

    class Meta:
        model = User
        fields = ["id", "email", "password", "is_superuser", "username"]
