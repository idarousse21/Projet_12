from django.contrib.auth.models import AbstractUser, BaseUserManager, Group, Permission
from django.db import models
from django.contrib.contenttypes.models import ContentType


CHOICES_USER_TEAM = [
    ("1", "Management team"),
    ("2", "Sales team"),
    ("3", "Support team"),
]


class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("L'adresse email doit être renseignée")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        return self.create_user(email, password, **extra_fields)


class User(AbstractUser):
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    email = models.EmailField(max_length=100, unique=True)
    user_team = models.CharField(max_length=50, choices=CHOICES_USER_TEAM)
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["first_name", "last_name", "user_team"]

    objects = UserManager()

    def save(self, *args, **kwargs):
        group = None
        if not self.username:
            self.username = self.email.lower()
        if self.user_team == "1":
            self.is_staff = True
            self.is_superuser = True

        self.set_password(self.password)
        super(User, self).save(*args, **kwargs)
        try:
            group = Group.objects.get(name=self.get_user_team_display())
            self.groups.add(group)
        except Group.DoesNotExist:
            group = Group.objects.create(name=self.get_user_team_display())
            client_content_type = ContentType.objects.get(
                app_label="project", model="client"
            )
            contract_content_type = ContentType.objects.get(
                app_label="project", model="contract"
            )
            event_content_type = ContentType.objects.get(
                app_label="project", model="event"
            )
            event_status_content_type = ContentType.objects.get(
                app_label="project", model="eventstatus"
            )
            view_client_permissions = Permission.objects.get(
                content_type=client_content_type, codename="view_client"
            )
            if self.user_team == "1":
                all_permissions = Permission.objects.all()
                group.permissions.add(*all_permissions)
            elif self.user_team == "2":
                add_client_permission = Permission.objects.get(
                    content_type=client_content_type, codename="add_client"
                )
                change_client_permission = Permission.objects.get(
                    content_type=client_content_type, codename="change_client"
                )
                view_contract_permissions = Permission.objects.get(
                    content_type=contract_content_type, codename="view_contract"
                )
                change_contract_permission = Permission.objects.get(
                    content_type=contract_content_type, codename="change_contract"
                )
                add_event_permission = Permission.objects.get(
                    content_type=event_content_type, codename="add_event"
                )
                group.permissions.add(
                    add_client_permission,
                    view_client_permissions,
                    change_client_permission,
                    view_contract_permissions,
                    change_contract_permission,
                    add_event_permission,
                )
            elif self.user_team == "3":
                view_event_permissions = Permission.objects.get(
                    content_type=event_content_type, codename="view_event"
                )
                change_event_permission = Permission.objects.get(
                    content_type=event_content_type, codename="change_event"
                )
                add_event_status_permission = Permission.objects.get(
                    content_type=event_status_content_type, codename="add_eventstatus"
                )
                change_event_status_permission = Permission.objects.get(
                    content_type=event_status_content_type,
                    codename="change_eventstatus",
                )
                group.permissions.add(
                    view_client_permissions,
                    view_event_permissions,
                    change_event_permission,
                    add_event_status_permission,
                    change_event_status_permission,
                )
            self.groups.add(group)
