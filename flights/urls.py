from django.urls import path

from .views import GenericFlightAPIView

urlpatterns = [
    path('', GenericFlightAPIView.as_view()),
    path('create/', GenericFlightAPIView.as_view()),
    path('detail/<int:id>/', GenericFlightAPIView.as_view())
]
