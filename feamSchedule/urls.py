from django.contrib import admin
from django.urls import path, include

from .views import (
    add_client_view,
    dashboard_view,
    appointments_view,
    clients_view
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', dashboard_view),
    path('clients/', clients_view),
    path('appointments/', appointments_view),
    path('add-client/', add_client_view),
    path('api/clients/', include('clients.urls')),
    path('api/appointments/', include('appointments.urls'))
]
