from django.contrib import admin
from django.urls import path, include

from .views import (
    add_client_view,
    dashboard_view
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', dashboard_view),
    path('add-client/', add_client_view),
    path('api/clients/', include('clients.urls'))
]
