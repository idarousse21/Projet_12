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
    exact_contract_date = filters.DateFilter(
        field_name="date_created", lookup_expr="exact"
    )
    contract_date_before = filters.DateFilter(
        field_name="date_created", lookup_expr="lte"
    )
    contract_date_after = filters.DateFilter(
        field_name="date_created", lookup_expr="gte"
    )
    exact_amount = filters.NumberFilter(field_name="amount", lookup_expr="exact")
    amount_above = filters.NumberFilter(field_name="amount", lookup_expr="gte")
    amount_below = filters.NumberFilter(field_name="amount", lookup_expr="lte")

    class Meta:
        model = Contract
        fields = [
            "last_name",
            "first_name",
            "email",
            "exact_contract_date",
            "contract_date_before",
            "contract_date_after",
            "exact_amount",
            "amount_above",
            "amount_below",
        ]


class EventFilter(filters.FilterSet):
    last_name = filters.CharFilter(
        field_name="client__last_name", lookup_expr="icontains"
    )
    first_name = filters.CharFilter(
        field_name="client__first_name", lookup_expr="icontains"
    )
    email = filters.CharFilter(field_name="client__email", lookup_expr="iexact")
    exact_event_date = filters.DateFilter(field_name="event_date", lookup_expr="exact")
    event_date_before = filters.DateFilter(field_name="event_date", lookup_expr="lte")
    event_date_after = filters.DateFilter(field_name="event_date", lookup_expr="gte")

    class Meta:
        model = Event
        fields = [
            "last_name",
            "first_name",
            "email",
            "exact_event_date",
            "event_date_before",
            "event_date_after",
        ]
