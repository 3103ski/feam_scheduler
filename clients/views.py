from .models import Client
from .forms import ClientForm
from django.shortcuts import render
from django.http import HttpResponse, Http404, JsonResponse


def client_create_view(request, *args, **kwargs):
    form = ClientForm(request.POST or None)
    print('the post data is: ', request.POST)
    if form.is_valid():
        obj = form.save(commit=False)
        obj.save()
        form = ClientForm()
    return render(request, "components/addClientForm.html", context={"form": form})


def client_list_view(request, *args, **kwargs):
    qs = Client.objects.all()
    client_list = [{"id": x.id, "name": x.name, "clientDescription": x.clientDescription,
                    "createdOn": x.createdOn, "lastModified": x.lastModified, "phoneNumber": x.phoneNumber, "address": x.address} for x in qs]
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
