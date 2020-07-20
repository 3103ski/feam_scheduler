from django.db import models
from django.contrib.auth import get_user_model
from staffMembers.models import StaffMember
from clients.models import Client

User = get_user_model()


def get_sentinel_user():
    return get_user_model().objects.get_or_create(username='deleted')[0]


class Flight(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE, null=True)
    flightNumber = models.CharField(null=False, max_length=6)
    tailNumber = models.CharField(null=False, max_length=6)
    parking = models.CharField(null=False, max_length=8)
    routing = models.TextField(null=False)
    flightDate = models.DateField(null=False)
    scheduledTOA = models.TimeField(null=False)
    scheduledTOD = models.TimeField(null=False)
    estimatedTOA = models.TimeField(null=False)
    estimatedTOD = models.TimeField(null=False)
    actualTOA = models.TimeField(null=True)
    actualTOD = models.TimeField(null=True)
    serviceDuration = models.CharField(null=True, blank=True, max_length=10)
    flightCoordinator = models.ForeignKey(
        StaffMember, on_delete=models.SET_NULL, related_name='flightCoordinator', blank=True, null=True)
    trafficCoordinator = models.ForeignKey(
        StaffMember, on_delete=models.SET_NULL,  related_name='trafficCoordinator', blank=True, null=True)
    # crew = Team
    lavService = models.ForeignKey(
        StaffMember, on_delete=models.SET_NULL, related_name='lavService', blank=True, null=True)
    remarks = models.TextField(null=True, blank=True)
    createdBy = models.ForeignKey(
        User, on_delete=models.SET(get_sentinel_user), null=True, blank=True)
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
            "flightDate": self.flightDate,
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
            "client": self.client
        }

    class Meta:
        ordering = ['flightDate']
