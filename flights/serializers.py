from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Flight
# from clients.models import Client
# from clients.serializers import ClientSerializer
# from staffMembers.serializers import StaffMemberSerializer


def get_sentinal_user():
    return get_user_model.objects.get_or_create(username='deleted')[0]


class ClientField(serializers.RelatedField):
    def to_representation(self, value):
        return value.name


class StaffMemberField(serializers.RelatedField):
    def to_representation(self, value):
        return value.name


class FlightSerializer(serializers.ModelSerializer):
    client = ClientField(read_only=True)
    lavService = StaffMemberField(read_only=True)
    flightCoordinator = StaffMemberField(read_only=True)
    trafficCoordinator = StaffMemberField(read_only=True)

    class Meta:
        model = Flight
        fields = ['client', 'flightNumber', 'tailNumber', 'parking', 'routing', 'flightDate', 'scheduledTOA', 'scheduledTOD', 'estimatedTOA', 'estimatedTOD',
                  'actualTOA', 'actualTOD', 'serviceDuration', 'flightCoordinator', 'trafficCoordinator', 'lavService', 'remarks', 'createdBy', 'createdOn', 'lastModified', 'id']
