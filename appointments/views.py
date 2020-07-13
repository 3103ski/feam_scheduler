from django.shortcuts import render

from .models import Appointment
from .forms import AppointmentForm

from django.shortcuts import render, redirect
from django.utils.http import is_safe_url
from django.http import HttpResponse, Http404, JsonResponse
from django.conf import settings

ALLOWED_HOSTS = settings.ALLOWED_HOSTS


def appointment_list_view(request, *args, **kwargs):
    qs = Appointment.objects.all()
    print("This is the dataset we are working with: ", qs)
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
