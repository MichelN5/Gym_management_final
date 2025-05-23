from django.contrib.auth.models import User
from rest_framework import serializers
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        write_only=True,
        min_length=8,  # Enforce minimum length
        required=True,
        style={'input_type': 'password'}
    )

    class Meta:
        model = User
        fields = ('id', 'username', 'password', 'is_superuser')
        extra_kwargs = {'password': {'write_only': True}}

    def validate_password(self, value):
        """Use Django's built-in password validation."""
        try:
            validate_password(value)  # Ensures the password meets Django's requirements
        except ValidationError as e:
            raise serializers.ValidationError(e.messages)
        return value

    def create(self, validated_data):
        """Create user with hashed password."""
        user = User.objects.create_user(**validated_data)
        return user
