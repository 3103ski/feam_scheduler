from django.contrib import admin
from django.urls import path, include
from django.views.i18n import JavaScriptCatalog

from .views import (
    add_client_view,
    add_appointment_view,
    dashboard_view,
    appointments_view,
    clients_view
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('jsi18n', JavaScriptCatalog.as_view(), name='js-catalog'),
    path('', dashboard_view),
    path('clients/', clients_view),
    path('appointments/', appointments_view),
    path('add-client/', add_client_view),
    path('add-appointment/', add_appointment_view),
    path('api/clients/', include('clients.urls')),
    path('api/appointments/', include('appointments.urls'))
]
