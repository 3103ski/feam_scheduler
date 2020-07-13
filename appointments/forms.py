
from django import forms
from .models import Appointment
from clients.models import Client
from django.contrib.admin.widgets import (
    AdminDateWidget,
    AdminTimeWidget
    # AdminSplitDateTime
)
import datetime


class AppointmentForm(forms.ModelForm):

    appointmentDate = forms.DateField(
        input_formats=['%Y-%m-%d'], widget=AdminDateWidget())
    appointmentTime = forms.TimeField(widget=AdminTimeWidget())

    class Meta:
        model = Appointment
        fields = ['appointmentDate', 'appointmentTime',
                  'appointmentNotes', 'client']

    def clean_client(self):
        client = self.cleaned_data['client']
        return client

    def clean_appointmentNotes(self):
        appointmentNotes = self.cleaned_data['appointmentNotes']
        return appointmentNotes

    def clean_appointmentDate(self):
        appointmentDate = self.cleaned_data['appointmentDate']
        return appointmentDate

    def clean_appointmentTime(self):
        appointmentTime = self.cleaned_data['appointmentTime']
        return appointmentTime
