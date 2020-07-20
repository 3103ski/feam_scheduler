from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


def get_sentinel_user():
    return get_user_model().objects.get_or_create(username='deleted')[0]


class Client(models.Model):
    # client info
    name = models.CharField(null=False, max_length=30)
    clientNotes = models.TextField(null=True, blank=True)
    address = models.CharField(null=True, max_length=100)
    contactNumber = models.IntegerField(null=False)

    # relational fields
    createdBy = models.ForeignKey(
        User, on_delete=models.SET(get_sentinel_user), null=True, blank=True)

    # Date Related
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
