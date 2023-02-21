from rest_framework.permissions import BasePermission
from django.shortcuts import get_object_or_404
from project.models import Client, Contract, Event, EventStatus

VIEW_AND_CREATE_HTTP_PERMISSIONS = ["GET", "POST"]
VIEW_AND_UPDATE_HTTP_PERMISSIONS = ["GET", "PUT", "PATCH"]


class ClientPermission(BasePermission):
    def has_permission(self, request, view):
        client = get_object_or_404(Client, id=view.kwargs["clients_pk"])
        if (
            request.method in VIEW_AND_CREATE_HTTP_PERMISSIONS
            and client.sales_contact == request.user
        ):
            return Client.objects.filter(sales_contact=request.user).exists()

    def has_object_permission(self, request, view, obj):
        if (
            request.method in VIEW_AND_UPDATE_HTTP_PERMISSIONS
            and obj.sales_contact == request.user
            and request.user.user_team == "Sales team"
        ):
            return Client.objects.filter(sales_contact=request.user).exists()
