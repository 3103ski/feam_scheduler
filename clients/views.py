# LOCAL
from .models import Client
from .serializers import ClientSerializer
# DJANGO
from django.shortcuts import redirect
from django.utils.http import is_safe_url
from django.conf import settings
# DRF
from rest_framework import generics
from rest_framework import mixins
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated

ALLOWED_HOSTS = settings.ALLOWED_HOSTS


class GenericClientAPIView(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, mixins.RetrieveModelMixin):
    serializer_class = ClientSerializer
    queryset = Client.objects.all()
    lookup_field = 'id'

    def get(self, request, id=None):
        if id:
            return self.retrieve(request)
        else:
            return self.list(request)

    def post(self, request):
        next_url = request.POST.get('next')
        if next_url != None and is_safe_url(next_url, ALLOWED_HOSTS):
            return self.create(request) and redirect(next_url)
        return self.create(request)

    def put(self, request, id=None):
        print('DID WE SEE AN ID HERE', id)
        return self.update(request, id)

    def delete(self, request, id):
        return self.destroy(request, id)
