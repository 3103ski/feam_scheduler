from django.urls import path
from .views import GenericStaffMemberAPIView

urlpatterns = [
    path('', GenericStaffMemberAPIView.as_view.()),
    path('create/', GenericStaffMemberAPIView.as_view()),
    path('detail/<int:id>/', GenericStaffMemberAPIView.as_view())
]
