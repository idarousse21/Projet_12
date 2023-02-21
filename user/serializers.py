from django.contrib.auth.models import Group
from user.models import User
from rest_framework.serializers import (
    ModelSerializer,
    CharField,
)
from django.contrib.auth.password_validation import validate_password


class UserSerializer(ModelSerializer):
    password = CharField(
        max_length=25,
        required=True,
        label="Mot de passe",
        validators=[
            validate_password,
        ],
    )

    class Meta:
        model = User
        fields = ("id", "first_name", "last_name", "email", "password", "user_team")

