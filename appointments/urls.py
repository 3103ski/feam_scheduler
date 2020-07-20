from django.urls import path

from .views import appointment_list_view, appointment_create_view, appointment_action_view


urlpatterns = [
    path('', appointment_list_view),
    path('create/', appointment_create_view),
    path('action/', appointment_action_view)
    # path('<int:appointment_id>/', appointment_detail_view),
    # path('<int:appointment_id>/delete', appointment_delete_view)
]
