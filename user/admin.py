from django.contrib import admin
from user.models import User


class UserAdminView(admin.ModelAdmin):
    model = User
    list_display = ["email", "first_name", "last_name", "user_team"]


admin.site.register(User, UserAdminView)
