from .models import Client
from .serializers import ClientSerializer
from .forms import ClientForm

from django.shortcuts import render, redirect
from django.utils.http import is_safe_url
from django.http import HttpResponse, Http404, JsonResponse
from django.conf import settings

from rest_framework.parsers import JSONParser

ALLOWED_HOSTS = settings.ALLOWED_HOSTS


def client_list(request):
    if request.method == 'GET':
        clients = Client.objects.all()
        serializer = ClientSerializer(clients, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        serializer = ClientSerializer(data=request.POST)
        next_url = request.POST.get('next')
        if serializer.is_valid():
            serializer.save()
            if next_url != None and is_safe_url(next_url, ALLOWED_HOSTS):
                return JsonResponse(serializer.data, status=201) and redirect(next_url)
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


def client_detail_view(request, client_id, *args, **kwargs):
    data = {
        "id": client_id,
    }
    status = 200
    try:
        obj = Client.objects.get(id=client_id)
        data['name'] = obj.name
        data['clientNotes'] = obj.clientNotes
        data['createdBy'] = obj.createdBy.username
        data['createdOn'] = obj.createdOn
        data['lastModified'] = obj.lastModified
        data['address'] = obj.address
        data['phoneNumber'] = obj.phoneNumber
    except:
        data['message'] = "Client Not Found"
        status = 404

    return JsonResponse(data, status=status)
