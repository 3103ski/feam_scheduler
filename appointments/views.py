from django.shortcuts import render

from .models import Appointment

from django.shortcuts import render, redirect
from django.utils.http import is_safe_url
from django.http import HttpResponse, Http404, JsonResponse
from django.conf import settings


def appointment_list_view(request, *args, **kwargs):
    qs = Appointment.objects.all()
    print("This is the dataset we are working with: ", qs)
    appointment_list = [x.serialize() for x in qs]
    data = {
        "response": appointment_list
    }
    return JsonResponse(data)
