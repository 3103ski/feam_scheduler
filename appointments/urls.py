from django.urls import path
from .views import (
    appointment_action_view,
    appointment_list
)


urlpatterns = [
    path('', appointment_list),
    path('create/', appointment_list),
    path('action/', appointment_action_view)
    # path('<int:appointment_id>/', appointment_detail_view),
    # path('<int:appointment_id>/delete', appointment_delete_view)
]
