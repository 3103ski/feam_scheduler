from django.shortcuts import render
from .models import Flight
from .serializers import FlightSerializer
from django.shortcuts import redirect
from django.utils.http import is_safe_url
from django.conf import settings

from rest_framework import generics
from rest_framework import mixins
from rest_framework.authentication import SessionAuthentication, BasicAuthentication

ALLOWED_HOSTS = settings.ALLOWED_HOSTS


class GenericFlightAPIView(generics.GenericAPIView, mixins.RetrieveModelMixin, mixins.ListModelMixin, mixins.CreateModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin):
    serializer_class = FlightSerializer
    queryset = Flight.objects.all()
    lookup_field = 'id'

    def get(self, request, id=None):
        if id:
            return self.retrieve(request)
        else:
            return self.list(request)

    def post(self, request):
        next_url = request.POST.get('next')
        if next_url != None and is_safe_url(next_url, ALLOWED_HOSTS):
            print(next_url, 'is safe')
            return self.create(request) and redirect(next_url)
        return self.create(request)

    def put(self, request, id):
        return self.update(request, id)

    def delete(self, request, id):
        return self.destroy(request, id)
