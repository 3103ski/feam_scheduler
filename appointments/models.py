from django.db import models
from django.contrib.auth import get_user_model
from clients.models import Client
User = get_user_model()


def get_sentinel_user():
    return get_user_model().objects.get_or_create(username='deleted')[0]


class Appointment(models.Model):

    # object fields and relationships
    client = models.ForeignKey(
        Client, on_delete=models.PROTECT)
    createdBy = models.ForeignKey(
        User, on_delete=models.SET(get_sentinel_user), null=True, blank=True)

    # text fields
    notes = models.TextField(null=True, blank=True)

    # datetime fields
    appointmentDate = models.DateTimeField(null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    lastModified = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['appointmentDate', '-id']

    # methods
    def __str__(self):
        return self.client.name

    def serialize(self):
        return {
            "client": self.client.name,
            "createdBy": self.createdBy.username,
            "appointmentDate": self.appointmentDate,
            "notes": self.notes,
            "createdOn": self.timestamp,
            "lastModified": self.lastModified
        }
