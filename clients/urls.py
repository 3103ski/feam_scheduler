from django.urls import path

from clients.views import (
    # client_list,
    # client_detail,
    # ClientAPIView,
    # ClientDetails,
    GenericClientAPIView
)


urlpatterns = [
    # path('<int:id>', ClientDetails.as_view()),
    path('', GenericClientAPIView.as_view()),
    path('<int:id>/', GenericClientAPIView.as_view()),
    # path('', GenericClientAPIView.as_view())
]
