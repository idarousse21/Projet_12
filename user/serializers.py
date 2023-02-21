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

    # def create(self, validated_data):
    #     user = User.objects.create_user(**validated_data)
    #     if validated_data["user_team"] == "1":
    #         validated_data["is_staff"] = True
    #         validated_data["is_superuser"] = True
    #     team = Group.objects.get(name=user.get_user_team_display())
    #     user.group.add(team)
    #     user.save()
    #     return user
