from django_filters import rest_framework as filters
from project.models import (
    Client,
    Contract,
    Event,
)


class ClientFilter(filters.FilterSet):
    last_name = filters.CharFilter(field_name="last_name", lookup_expr="icontains")
    first_name = filters.CharFilter(field_name="first_name", lookup_expr="icontains")
    email = filters.CharFilter(field_name="email", lookup_expr="iexact")

    class Meta:
        model = Client
        fields = ["last_name", "first_name", "email"]


class ContractFilter(filters.FilterSet):
    last_name = filters.CharFilter(
        field_name="client__last_name", lookup_expr="icontains"
    )
    first_name = filters.CharFilter(
        field_name="client__first_name", lookup_expr="icontains"
    )
    email = filters.CharFilter(field_name="client__email", lookup_expr="iexact")

    class Meta:
        model = Contract
        fields = ["last_name", "first_name", "email"]


class EventFilter(filters.FilterSet):
    last_name = filters.CharFilter(
        field_name="client__last_name", lookup_expr="icontains"
    )
    first_name = filters.CharFilter(
        field_name="client__first_name", lookup_expr="icontains"
    )
    email = filters.CharFilter(field_name="client__email", lookup_expr="iexact")
