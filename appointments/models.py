from django.db import models
from django.contrib.auth import get_user_model
from clients.models import Client
from .utils import AppointmentStatusTypes
User = get_user_model()


def get_sentinel_user():
    return get_user_model().objects.get_or_create(username='deleted')[0]


class Appointment(models.Model):
    # relationships
    client = models.ForeignKey(
        Client, on_delete=models.SET_NULL, related_name='appointment', null=True, blank=True)
    # text fields
    appointmentNotes = models.TextField(blank=True)
    # datetime fields
    appointmentDate = models.DateField(null=True, blank=True)
    appointmentTime = models.TimeField(null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    lastModified = models.DateTimeField(auto_now=True)
    # enums
    status = models.IntegerField(choices=AppointmentStatusTypes.choices(
    ), default=AppointmentStatusTypes.NOT_STARTED)

    class Meta:
        ordering = ['appointmentDate', 'appointmentTime', '-id']

    def __str__(self):
        return str(self.client)

    def get_status(self):
        return AppointmentStatusTypes(self.status).name.title()

    def serialize(self):
        return {
            "appointmentDate": self.appointmentDate,
            "appointmentTime": self.appointmentTime,
            "createdOn": self.timestamp,
            "lastModified": self.lastModified,
            "appointmentNotes": self.appointmentNotes,
            "client": self.client.name,
            "id": self.id
        }
