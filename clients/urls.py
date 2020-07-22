from django.contrib import admin
from django.urls import path

from clients.views import (
    client_list,
    client_detail_view,
)


urlpatterns = [
    path('', client_list),
    path('<int:client_id>', client_detail_view),
    path('create/', client_list),
]
