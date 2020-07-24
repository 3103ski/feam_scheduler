from django.urls import path

from .views import flight_list, flight_detail

urlpatterns = [
    path('', flight_list),
    path('detail/<int:pk>/', flight_detail),
    path('create/', flight_list)
]
