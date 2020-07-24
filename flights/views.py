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
        serializer = FlightSerializer(data=request.POST)
        next_url = request.POST.get('next')
        if serializer.is_valid():
            serializer.save()
            if next_url != None and is_safe_url(next_url, ALLOWED_HOSTS):
                return JsonResponse(serializer.data, status=201) and redirect(next_url)
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


def flight_detail(request, pk):
    try:
        flight = Flight.objects.get(pk=pk)
    except Flight.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = FlightSerializer(flight)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = FlightSerializer(article, data=data)
        if serializer.is_valid():
            serializer.save()
            if next_url != None and is_safe_url(next_url, ALLOWED_HOSTS):
                return JsonResponse(serializer.data, status=201) and redirect(next_url)
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        flight.delete()
        return HttpResponse(status=204)


def flight_action(request):
    print(request.data)
    # action = request.data.action
    # flight_id = request.data.id

    # if action == 'delete':
    #     Flight.objects.delete(id=flight_id)
    return redirect('/flights/')
