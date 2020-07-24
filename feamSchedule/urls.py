from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token

from .views import (
    add_client_view,
    dashboard_view,
    clients_view,
    flights_view,
    add_flight_view
)

from django.views.i18n import JavaScriptCatalog

urlpatterns = [
    path('admin/', admin.site.urls),
    path('jsi18n', JavaScriptCatalog.as_view(), name='js-catalog'),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
    path('', dashboard_view),
    path('clients/', clients_view),
    path('flights/', flights_view),
    path('add-client/', add_client_view),
    path('add-flight/', add_flight_view),
    path('api/clients/', include('clients.urls')),
    path('api/flights/', include('flights.urls')),
    path('flights/api/flights/', include('flights.urls'))
]
