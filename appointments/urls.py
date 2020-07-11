from django.urls import path

from .views import appointment_list_view


urlpatterns = [
    path('', appointment_list_view)
]
