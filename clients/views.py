from django.shortcuts import render
from django.http import HttpResponse, Http404, JsonResponse

from .models import Client


def home_view(request, *args, **kwargs):
    return render(request, "pages/home.html", context={}, status=200)


def client_list_view(request, *args, **kwargs):
    qs = Client.objects.all()
    client_list = [{"id": x.id, "name": x.name, "createdBy": x.createdBy.username,
                    "createdOn": x.createdOn, "lastModified": x.lastModified} for x in qs]
    data = {
        "response": client_list
    }
    return JsonResponse(data)


def client_detail_view(request, client_id, *args, **kwargs):
    data = {
        "id": client_id,
    }
    status = 200
    try:
        obj = Client.objects.get(id=client_id)
        data['name'] = obj.name
        data['createdBy'] = obj.createdBy.username
        data['createdOn'] = obj.createdOn
        data['lastModified'] = obj.lastModified
    except:
        data['message'] = "Client Not Found"
        status = 404

    return JsonResponse(data, status=status)
