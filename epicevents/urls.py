"""epicevents URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from user.views import SignupView
from rest_framework_simplejwt.views import (
    TokenRefreshView,
    TokenObtainPairView,
)
from rest_framework_nested import routers
from project.views import ClientView, ContractView, EventView, EventStatusView

client_router = routers.SimpleRouter()
client_router.register(r"clients", ClientView, basename="clients")

contract_router = routers.SimpleRouter()
contract_router.register(r"contracts", ContractView, basename="contracts")

event_router = routers.SimpleRouter()
event_router.register(r"events", EventView, basename="events")

event_status_router = routers.SimpleRouter()
event_status_router.register(
    r"events_status", EventStatusView, basename="events_status"
)


urlpatterns = [
    path("admin/", admin.site.urls),
    path("signup/", SignupView.as_view(), name="signup"),
    path("login/", TokenObtainPairView.as_view(), name="login"),
    path("", include(client_router.urls)),
    path("", include(contract_router.urls)),
    path("", include(event_router.urls)),
    path("", include(event_status_router.urls)),
]
