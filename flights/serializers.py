from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Flight


def get_sentinal_user():
    return get_user_model.objects.get_or_create(username='deleted')[0]


class FlightSerializer(serializers.ModelSerializer):
    class Meta:
        model = Flight
        fields = ['client', 'flightNumber', 'tailNumber', 'parking', 'routing', 'flightDate', 'scheduledTOA', 'scheduledTOD', 'estimatedTOA', 'estimatedTOD',
                  'actualTOA', 'actualTOD', 'serviceDuration', 'flightCoordinator', 'trafficCoordinator', 'lavService', 'remarks', 'createdBy', 'createdOn', 'lastModified']
