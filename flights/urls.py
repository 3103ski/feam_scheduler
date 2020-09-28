from django.urls import path

from .views import GenericFlightAPIView

urlpatterns = [
    path('', GenericFlightAPIView.as_view()),
    path('<int:id>/', GenericFlightAPIView.as_view())
]
