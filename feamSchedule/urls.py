from django.contrib import admin
from django.urls import path, include

from .views import (
    add_client_view,
    add_appointment_view,
    dashboard_view,
    appointments_view,
    clients_view,
    flights_view,
    add_flight_view
)

from django.views.i18n import JavaScriptCatalog

urlpatterns = [
    path('admin/', admin.site.urls),
    path('jsi18n', JavaScriptCatalog.as_view(), name='js-catalog'),
    path('', dashboard_view),
    path('clients/', clients_view),
    path('flights/', flights_view),
    path('appointments/', appointments_view),
    path('appointments/api/appointments/', include('appointments.urls')),
    path('add-client/', add_client_view),
    path('add-appointment/', add_appointment_view),
    path('add-flight/', add_flight_view),
    path('api/clients/', include('clients.urls')),
    path('api/flights/', include('flights.urls')),
    path('api/appointments/', include('appointments.urls'))
]
