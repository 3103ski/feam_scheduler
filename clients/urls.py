from django.urls import path

from clients.views import (
    GenericClientAPIView
)


urlpatterns = [
    path('', GenericClientAPIView.as_view()),
    path('<int:id>/', GenericClientAPIView.as_view()),
]
