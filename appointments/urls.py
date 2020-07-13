from django.urls import path

from .views import appointment_list_view, appointment_create_view


urlpatterns = [
    path('', appointment_list_view),
    path('create/', appointment_create_view)
]
