from django.db import models
from django.contrib.auth import get_user_model
from clients.models import Client
User = get_user_model()


def get_sentinel_user():
    return get_user_model().objects.get_or_create(username='deleted')[0]


class Appointment(models.Model):
    client = models.ForeignKey(
        Client, on_delete=models.PROTECT)

    createdBy = models.ForeignKey(
        User, on_delete=models.SET(get_sentinel_user), null=True, blank=True)

    appointmentDate = models.DateTimeField()
    notes = models.TextField(null=True, blank=True)

    timestamp = models.DateTimeField(auto_now_add=True)
    lastModified = models.DateField(auto_now=True)

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return self.client.name
