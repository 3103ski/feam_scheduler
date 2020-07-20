from django.contrib import admin
from django.urls import path, include

from .views import (
    add_client_view,
    add_appointment_view,
    dashboard_view,
    appointments_view,
    clients_view
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', dashboard_view),
    path('clients/', clients_view),
    path('appointments/', appointments_view),
    path('appointments/api/appointments/', include('appointments.urls')),
    path('add-client/', add_client_view),
    path('add-appointment/', add_appointment_view),
    path('api/clients/', include('clients.urls')),
    path('api/appointments/', include('appointments.urls'))
]
