from django import forms
from .models import Flight
from clients.models import Client
from clients.serializers import ClientSerializer
from staffMembers.serializers import StaffMemberSerializer

from django.contrib.admin.widgets import (
    AdminDateWidget,
    AdminTimeWidget
    # AdminSplitDateTime
)
import datetime


class FlightForm(forms.ModelForm):

    flightDate = forms.DateField(
        input_formats=['%Y-%m-%d'], widget=AdminDateWidget())

    scheduledTOA = forms.TimeField(widget=AdminTimeWidget())
    scheduledTOD = forms.TimeField(widget=AdminTimeWidget())
    estimatedTOA = forms.TimeField(widget=AdminTimeWidget())
    estimatedTOD = forms.TimeField(widget=AdminTimeWidget())
    actualTOA = forms.TimeField(widget=AdminTimeWidget())
    actualTOD = forms.TimeField(widget=AdminTimeWidget())

    class Meta:
        model = Flight
        fields = fields = ['client', 'flightNumber', 'tailNumber', 'parking', 'routing', 'flightDate', 'scheduledTOA', 'scheduledTOD', 'estimatedTOA', 'estimatedTOD',
                           'actualTOA', 'actualTOD', 'serviceDuration', 'flightCoordinator', 'trafficCoordinator', 'lavService', 'remarks', 'createdBy']

    def clean_client(self):
        # client = self.cleaned_data('client')
        client = ClientSerializer()
        return client

    def clean_flightNumber(self):
        flightNumber = self.cleaned_data('flightNumber')
        return flightNumber

    def clean_tailNumber(self):
        tailNumber = self.cleaned_data('tailNumber')
        return tailNumber

    def clean_parking(self):
        parking = self.cleaned_data('parking')
        return parking

    def clean_routing(self):
        routing = self.cleaned_data('routing')
        return routing

    def clean_flightDate(self):
        flightDate = self.cleaned_data('flightDate')
        return flightDate

    def clean_scheduledTOA(self):
        scheduledTOA = self.cleaned_data('scheduledTOA')
        return scheduledTOA

    def clean_scheduledTOD(self):
        scheduledTOD = self.cleaned_data('scheduledTOD')
        return scheduledTOD

    def clean_estimatedTOA(self):
        estimatedTOA = self.cleaned_data('estimatedTOA')
        return estimatedTOA

    def clean_estimatedTOD(self):
        estimatedTOD = self.cleaned_data('estimatedTOD')
        return estimatedTOD

    def clean_actualTOA(self):
        actualTOA = self.cleaned_data('actualTOA')
        return actualTOA

    def clean_actualTOD(self):
        actualTOD = self.cleaned_data('actualTOD')
        return actualTOD

    def clean_serviceDuration(self):
        serviceDuration = self.cleaned_data('serviceDuration')
        return serviceDuration

    def clean_flightCoordinator(self):
        flightCoordinator = self.cleaned_data('flightCoordinator')
        return flightCoordinator

    def clean_trafficCoordinator(self):
        trafficCoordinator = self.cleaned_data('trafficCoordinator')
        return trafficCoordinator

    def clean_lavService(self):
        lavService = self.cleaned_data('lavService')
        return lavService

    def clean_remarks(self):
        remarks = self.cleaned_data('remarks')
        return remarks

    def clean_createdBy(self):
        createdBy = self.cleaned_data('createdBy')
        return createdBy
