from rest_framework.permissions import IsAuthenticated
from rest_framework.filters import SearchFilter
from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response
from rest_framework import status


from project.models import (
    Client,
    Contract,
    Event,
    EventStatus,
)
from project.serializers import (
    ClientViewSerializer,
    ClientPostAndUpdateSerializer,
    ContractViewSerializer,
    ContractPostAndUpdateSerializer,
    EventViewSerializer,
    EventPostAndUpdateSerializer,
    EventStatusSerializer,
)
from project.permissions import (
    ClientPermission,
    ContractPermission,
    EventPermission,
    EventStatusPermission,
)
from project.filter_search import ClientFilter, ContractFilter, EventFilter

VIEW_HTTP_REQUEST = ["GET"]
CREATE_AND_UPDATE_HTTP_REQUEST = ["POST", "PUT", "PATCH"]
STATUS_HTTP_OK = status.HTTP_200_OK
STATUS_HTTP_BAD_REQUEST = status.HTTP_400_BAD_REQUEST


class ClientView(ModelViewSet):
    permission_classes = [
        IsAuthenticated,
        ClientPermission,
    ]
    serializer_class = ClientViewSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_class = ClientFilter
    search_fields = ["last_name", "first_name", "email"]

    def get_queryset(self):
        clients = Client.objects.all()
        if self.request.user.user_team == "1":
            return clients
        elif self.request.user.user_team == "2":
            return clients.filter(sales_contact=self.request.user).distinct()
        elif self.request.user.user_team == "3":
            return clients.filter(event__support_contact=self.request.user).distinct()

    def get_serializer_class(self):
        if self.request.method in CREATE_AND_UPDATE_HTTP_REQUEST:
            return ClientPostAndUpdateSerializer
        else:
            return ClientViewSerializer

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context["user_team"] = self.request.user.user_team
        return context


class ContractView(ModelViewSet):
    permission_classes = [IsAuthenticated, ContractPermission]
    serializer_class = ContractViewSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_class = ContractFilter
    search_fields = ["client__first_name", "client__last_name", "client__email"]

    def get_queryset(self):
        contract = Contract.objects.all()
        if self.request.user.user_team == "1":
            return contract
        elif self.request.user.user_team == "2":
            return contract.filter(sales_contact=self.request.user).distinct()

    def get_serializer_class(self):
        if self.request.method in CREATE_AND_UPDATE_HTTP_REQUEST:
            return ContractPostAndUpdateSerializer
        else:
            return ContractViewSerializer

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context["user_team"] = self.request.user.user_team
        return context


class EventView(ModelViewSet):
    permission_classes = [IsAuthenticated, EventPermission]
    serializer_class = EventViewSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_class = EventFilter
    search_fields = ["client__first_name", "client__last_name", "client__email"]

    def get_queryset(self):
        event = Event.objects.all()
        if self.request.user.user_team == "1":
            return event
        elif self.request.user.user_team == "3":
            return event.filter(support_contact=self.request.user).distinct()

    def get_serializer_class(self):
        if self.request.method in CREATE_AND_UPDATE_HTTP_REQUEST:
            return EventPostAndUpdateSerializer
        else:
            return EventViewSerializer

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context["user_team"] = self.request.user.user_team
        return context


class EventStatusView(ModelViewSet):
    permission_classes = [IsAuthenticated, EventStatusPermission]
    serializer_class = EventStatusSerializer

    def get_queryset(self):
        return EventStatus.objects.all()
