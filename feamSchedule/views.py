from django.shortcuts import render


def dashboard_view(request, *args, **kwargs):
    return render(request, "pages/dashboard.html", context={}, status=200)


def add_client_view(request, *args, **kwargs):
    return render(request, "pages/addClient.html", context={}, status=200)
