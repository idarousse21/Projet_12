from rest_framework.serializers import ModelSerializer, ValidationError
from project.models import (
    Client,
    Contract,
    Event,
    EventStatus,
)
from rest_framework.generics import get_object_or_404


# créer une mixin validate
class MixinValidateSalesContact:
    def validate_sales_contact(self, sales_contact):
        if (
            self.instance
            and self.instance.sales_contact != sales_contact
            and self.user_team != "1"
        ):
            return self.instance.sales_contact
        elif not self.instance and self.user_team != "1":
            return None
        else:
            return sales_contact


class ClientViewSerializer(ModelSerializer):
    class Meta:
        model = Client
        fields = "__all__"


class ClientPostAndUpdateSerializer(MixinValidateSalesContact, ModelSerializer):
    class Meta:
        model = Client
        fields = [
            "id",
            "first_name",
            "last_name",
            "email",
            "phone",
            "mobile",
            "sales_contact",
        ]

    def __init__(self, *args, **kwargs):
        self.user_team = kwargs["context"].pop("user_team")
        super().__init__(*args, **kwargs)


class ContractViewSerializer(ModelSerializer):
    class Meta:
        model = Contract
        fields = "__all__"


class ContractPostAndUpdateSerializer(MixinValidateSalesContact, ModelSerializer):
    class Meta:
        model = Contract
        fields = ["id", "sales_contact", "client", "status", "amount", "payment_due"]

    def __init__(self, *args, **kwargs):
        self.user_team = kwargs["context"].pop("user_team")
        super().__init__(*args, **kwargs)


class EventViewSerializer(ModelSerializer):
    class Meta:
        model = Event
        fields = "__all__"


class EventPostAndUpdateSerializer(ModelSerializer):
    class Meta:
        model = Event
        fields = [
            "id",
            "contract",
            "support_contact",
            "event_status",
            "attendees",
            "event_date",
            "notes",
        ]

    def __init__(self, *args, **kwargs):
        self.user_team = kwargs["context"].pop("user_team")
        return super().__init__(*args, **kwargs)

    def validate_support_contact(self, support_contact):
        if (
            self.instance
            and self.instance.support_contact != support_contact
            and self.user_team != "1"
        ):
            return self.instance.support_contact
        elif not self.instance and self.user_team != "1":
            return None
        else:
            return support_contact

    def save(self, **kwargs):
        contract = get_object_or_404(Contract, id=self.validated_data["contract"].id)
        if contract.status:
            self.validated_data["client"] = contract.client
            return super().save(**kwargs)
        else:
            raise ValidationError(
                "The contract status is not valid, please validate the contract status before creating the event."
            )


class EventStatusSerializer(ModelSerializer):
    class Meta:
        model = EventStatus
        fields = "__all__"
