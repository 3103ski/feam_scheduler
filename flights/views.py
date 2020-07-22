from django.shortcuts import render

from .models import Flight
from .serializers import FlightSerializer
from .forms import FlightForm

from django.shortcuts import render, redirect
from django.utils.http import is_safe_url
from django.http import HttpResponse, Http404, JsonResponse
from django.conf import settings

from rest_framework.response import Response
from rest_framework.authentication import SessionAuthentication
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import IsAuthenticated

ALLOWED_HOSTS = settings.ALLOWED_HOSTS


def flight_list(request):
    if request.method == 'GET':
        flights = Flight.objects.all()
        serializer = FlightSerializer(flights, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        # form = FlightForm(request.POST or None)
        serializer = FlightSerializer(data=request.POST)
        next_url = request.POST.get('next')
        if serializer.is_valid():
            serializer.save()
            if next_url != None and is_safe_url(next_url, ALLOWED_HOSTS):
                return JsonResponse(serializer.data, status=201) and redirect(next_url)
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)
