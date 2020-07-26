from django.db import models
from django.contrib.auth import get_user_model
from django.conf import settings

User = settings.AUTH_USER_MODEL


def get_sentinel_user():
    return get_user_model().objects.get_or_create(username='deleted')[0]


class StaffMember(models.Model):
    name = models.TextField(null=False)
    position = models.TextField(null=False)
    createdBy = models.ForeignKey(
        User, related_name='staffMembers', on_delete=models.SET(get_sentinel_user), null=True, blank=True)
    createdOn = models.DateTimeField(auto_now_add=True)
    lastModified = models.DateTimeField(auto_now=True)
    contactNumber = models.IntegerField(null=True)
    emailAddress = models.EmailField(null=False)
    team = models.TextField(null=True)
    supervisor = models.ForeignKey(
        'self', on_delete=models.SET_NULL, related_name='staffMember', null=True, blank=True)

    def __str__(self):
        return self.name

    def serialize(self):
        return {
            "name": self.name,
            "position": self.position,
            "createdBy": self.createdBy,
            "createdOn": self.createdOn,
            "lastModified": self.lastModified,
            "contactNumber": self.contactNumber,
            "emailAddress": self.emailAddress,
            "supervisor": self.supervisor,
            "team": self.team,
            "id": self.id
        }
