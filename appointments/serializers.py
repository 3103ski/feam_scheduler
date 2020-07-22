from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Appointment


def get_sentinal_user():
    return get_user_model.objects.get_or_create(username='deleted')[0]


class AppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields = ['client', 'appointmentNotes', 'appointmentDate',
                  'appointmentTime', 'timestamp', 'lastModified', 'status']
