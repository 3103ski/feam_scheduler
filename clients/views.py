from .models import Client
from .forms import ClientForm

from django.shortcuts import render, redirect
from django.utils.http import is_safe_url
from django.http import HttpResponse, Http404, JsonResponse
from django.conf import settings


ALLOWED_HOSTS = settings.ALLOWED_HOSTS


def client_create_view(request, *args, **kwargs):
    # print("ajax", request.is_ajax())
    print(request.POST)
    form = ClientForm(request.POST or None)
    next_url = request.POST.get('next') or None
    if form.is_valid():
        obj = form.save(commit=False)
        obj.save()
        if request.is_ajax():
            return JsonResponse(obj.serialize(), status=201)
        if next_url != None and is_safe_url(next_url, ALLOWED_HOSTS):
            return redirect(next_url)
        form = ClientForm()
    return render(request, "components/clients/addClientForm.html", context={"form": form})


def client_list_view(request, *args, **kwargs):
    qs = Client.objects.all()
    client_list = [x.serialize() for x in qs]
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
        data['clientDescription'] = obj.clientDescription
        data['createdBy'] = obj.createdBy.username
        data['createdOn'] = obj.createdOn
        data['lastModified'] = obj.lastModified
        data['address'] = obj.address
        data['phoneNumber'] = obj.phoneNumber
    except:
        data['message'] = "Client Not Found"
        status = 404

    return JsonResponse(data, status=status)
