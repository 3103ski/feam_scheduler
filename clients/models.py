from django.db import models
from django.contrib.auth import get_user_model
from django.conf import settings

User = settings.AUTH_USER_MODEL


def get_sentinel_user():
    return get_user_model().objects.get_or_create(username='deleted')[0]


class Client(models.Model):
    name = models.CharField(null=False, max_length=30)
    clientNotes = models.CharField(max_length=500, null=True, blank=True)
    address = models.CharField(null=True, max_length=100)
    contactNumber = models.IntegerField(null=False)
    createdBy = models.ForeignKey(
        User, related_name='clients', on_delete=models.SET(get_sentinel_user), null=True, blank=True)
    createdOn = models.DateTimeField(auto_now_add=True)
    lastModified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "address": self.address,
            "contactNumber": self.contactNumber,
            "clientNotes": self.clientNotes,
            "createdBy": self.createdBy,
            "createdOn": self.createdOn,
            "lastModified": self.lastModified
        }

    class Meta:
        ordering = ['name']
