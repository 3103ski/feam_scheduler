from django.shortcuts import render
from appointments.forms import AppointmentForm


def dashboard_view(request, *args, **kwargs):
    return render(request, "pages/dashboard.html", context={}, status=200)


def clients_view(request, *args, **kwargs):
    return render(request, "pages/clients.html", context={}, status=200)


def appointments_view(request, *args, **kwargs):
    return render(request, "pages/appointments.html", context={}, status=200)


def add_client_view(request, *args, **kwargs):
    return render(request, "pages/addClient.html", context={}, status=200)


def add_appointment_view(request, *args, **kwargs):
    return render(request, "pages/addAppointment.html", context={"form": AppointmentForm}, status=200)
