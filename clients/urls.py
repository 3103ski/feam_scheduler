from django.contrib import admin
from django.urls import path

from clients.views import (
    client_list_view,
    client_create_view,
    client_detail_view,
)


urlpatterns = [
    path('', client_list_view),
    path('<int:client_id>', client_detail_view),
    path('create/', client_create_view),
]
