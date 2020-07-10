from django.contrib import admin
from django.urls import path
from clients.views import client_list_view, client_detail_view, home_view

urlpatterns = [
    path('', home_view),
    path('admin/', admin.site.urls),
    path('clients/', client_list_view),
    path('clients/<int:client_id>', client_detail_view)
]
