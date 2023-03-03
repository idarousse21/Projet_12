from rest_framework.permissions import BasePermission
from django.shortcuts import get_object_or_404
from project.models import Client, Contract, Event, EventStatus

VIEW_AND_CREATE_HTTP_REQUEST = ["GET", "POST"]
VIEW_AND_UPDATE_HTTP_REQUEST = ["GET", "PUT", "PATCH"]
VIEW_HTTP_REQUEST = ["GET"]
CREATE_HTTP_REQUEST = ["POST"]


class ClientPermission(BasePermission):
    def has_permission(self, request, view):
        if request.user.user_team == "1":
            return True
        elif request.user.user_team == "2":
            return request.method != "DELETE"
        elif request.user.user_team == "3":
            return request.method == "GET"

    def has_object_permission(self, request, view, obj):
        if request.user.user_team == "1":
            return True
        elif request.user.user_team == "2":
            return obj.sales_contact == request.user
        elif request.user.user_team == "3":
            return Client.objects.filter(event__support_contact=request.user).exists()
        


class ContractPermission(BasePermission):
    def has_permission(self, request, view):
        if request.user.user_team == "1":
            return True
        elif request.user.user_team == "2":
            return request.method != "DELETE"

    def has_object_permission(self, request, view, obj):
        if request.user.user_team == "1":
            return True
        elif request.user.user_team == "2":
            return obj.sales_contact == request.user


class EventPermission(BasePermission):
    def has_permission(self, request, view):
        if request.user.user_team == "1":
            return True
        elif request.user.user_team == "2":
            return request.method == "POST"
        elif request.user.user_team == "3" and request.method in VIEW_AND_UPDATE_HTTP_REQUEST:
            return True

    def has_object_permission(self, request, view, obj):
        if request.user.user_team == "1":
            return True
        elif request.user.user_team == "3":
            return obj.support_contact == request.user


class EventStatusPermission(BasePermission):
    def has_permission(self, request, view):
        if request.user.user_team == "1":
            return True
        elif request.user.user_team == "3":
            return request.method != "DELETE"

    def has_object_permission(self, request, view, obj):
        if request.user.user_team == "1":
            return True
        elif request.user.user_team == "3":
            return True
