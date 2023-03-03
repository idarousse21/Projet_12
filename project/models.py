from django.db import models
from django.conf import settings
from django.core.validators import MinValueValidator


class Client(models.Model):
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    email = models.EmailField(
        max_length=100,
        unique=True,
    )
    phone = models.CharField(max_length=20)
    mobile = models.CharField(max_length=20)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    sales_contact = models.ForeignKey(
        to=settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True
    )


class Contract(models.Model):
    sales_contact = models.ForeignKey(
        to=settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True
    )
    client = models.ForeignKey(to=Client, on_delete=models.CASCADE, null=False)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=False)
    amount = models.FloatField(null=True)
    payment_due = models.DateField()


class EventStatus(models.Model):
    title = models.CharField(max_length=25)
    description = models.CharField(max_length=250)


class Event(models.Model):
    client = models.ForeignKey(to=Client, on_delete=models.CASCADE, null=True)
    contract = models.ForeignKey(to=Contract, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    support_contact = models.ForeignKey(
        to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True
    )
    event_status = models.ForeignKey(
        to=EventStatus, on_delete=models.SET_NULL, null=True
    )
    attendees = models.IntegerField(MinValueValidator(0))
    event_date = models.DateTimeField()
    notes = models.TextField(max_length=5000, null=True)
