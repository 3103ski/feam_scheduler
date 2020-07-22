from django.shortcuts import render

from .models import Appointment
from .forms import AppointmentForm
from .serializers import AppointmentSerializer

from django.shortcuts import render, redirect
from django.utils.http import is_safe_url
from django.http import HttpResponse, Http404, JsonResponse
from django.conf import settings

from rest_framework.response import Response
from rest_framework.authentication import SessionAuthentication
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import IsAuthenticated

ALLOWED_HOSTS = settings.ALLOWED_HOSTS


def appointment_list(request):
    if request.method == 'GET':
        appointments = Appointment.objects.all()
        serializer = AppointmentSerializer(appointments, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        serializer = AppointmentSerializer(data=request.POST)
        next_url = request.POST.get('next')
        if serializer.is_valid():
            serializer.save()
            if next_url != None and is_safe_url(next_url, ALLOWED_HOSTS):
                return JsonResponse(serializer.data, status=201) and redirect(next_url)
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


def appointment_list_view(request, *args, **kwargs):
    qs = Appointment.objects.all()
    appointment_list = [x.serialize() for x in qs]
    data = {
        "response": appointment_list
    }
    return JsonResponse(data)


def appointment_create_view(request, *args, **kwargs):
    form = AppointmentForm(request.POST or None)
    next_url = request.POST.get('next') or None
    if form.is_valid():
        print('THE MOST VALID ISH EVER')
        obj = form.save(commit=False)
        obj.save()
        if request.is_ajax():
            return JsonResponse(obj.serialize(), status=201)
        if next_url != None and is_safe_url(next_url, ALLOWED_HOSTS):
            return redirect(next_url)
        form = AppointmentForm()
    return render(request, "components/appointments/addAppointmentForm.html", context={"form": form})


def appointment_action_view(request, *args, **kwargs):
    qs = Appointment.objects.all()
    # appointment = qs.filter(id=appointment_id)
    print('this is the data set', qs)
    print('this is the request', request.data)
    return render(request, "pages/appointments.html", context={})
