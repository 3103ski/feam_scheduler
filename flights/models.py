from django.db import models
from django.contrib.auth import get_user_model
from staffMembers.models import StaffMember
from clients.models import Client

User = get_user_model()


def get_sentinel_user():
    return get_user_model().objects.get_or_create(username='deleted')[0]


class Flight(models.Model):
    client = models.ForeignKey(
        Client, on_delete=models.CASCADE, null=True, blank=True)
    flightNumber = models.CharField(null=False, max_length=60)
    tailNumber = models.CharField(null=False, max_length=60)
    parking = models.CharField(null=False, max_length=80)
    routing = models.TextField(null=False)
    scheduledTOA = models.DateTimeField(null=True, blank=True)
    scheduledTOD = models.DateTimeField(null=True, blank=True)
    estimatedTOA = models.DateTimeField(null=True, blank=True)
    estimatedTOD = models.DateTimeField(null=True, blank=True)
    actualTOA = models.DateTimeField(null=True, blank=True)
    actualTOD = models.DateTimeField(null=True, blank=True)
    serviceDuration = models.CharField(null=True, blank=True, max_length=10)
    flightCoordinator = models.ForeignKey(
        StaffMember, on_delete=models.SET_NULL, related_name='flightCoordinator', blank=True, null=True)
    trafficCoordinator = models.ForeignKey(
        StaffMember, on_delete=models.SET_NULL,  related_name='trafficCoordinator', blank=True, null=True)
    lavService = models.ForeignKey(
        StaffMember, on_delete=models.SET_NULL, related_name='lavService',  null=True, blank=True)
    remarks = models.TextField(null=True, blank=True)
    createdBy = models.ForeignKey(
        User, related_name='flights', on_delete=models.SET(get_sentinel_user), null=True, blank=True)
    createdOn = models.DateTimeField(auto_now_add=True)
    lastModified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "Flight Number: " + self.flightNumber

    def serialize(self):
        return {
            "flightNumber": self.flightNumber,
            "tailNumber": self.tailNumber,
            "parking": self.parking,
            "routing": self.routing,
            "scheduledTOA": self.scheduledTOA,
            "scheduledTOD": self.scheduledTOD,
            "estimatedTOA": self.estimatedTOA,
            "estimatedTOA": self.estimatedTOA,
            "actualTOA": self.actualTOA,
            "actualTOD": self.actualTOD,
            "serviceDuration": self.serviceDuration,
            "remarks": self.remarks,
            "createdBy": self.createdBy,
            "createdOn": self.createdOn,
            "lastModified": self.lastModified,
            "flightCoordinator": self.flightCoordinator,
            "trafficCoordinator": self.trafficCoordinator,
            "lavService": self.lavService,
            "client": self.client.name,
            "id": self.id
        }

    class Meta:
        ordering = ['scheduledTOA']
