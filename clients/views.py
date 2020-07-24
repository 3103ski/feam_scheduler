from .models import Client
from .serializers import ClientSerializer
from .forms import ClientForm

from django.shortcuts import render, redirect
from django.utils.http import is_safe_url
from django.http import HttpResponse, Http404, JsonResponse
from django.conf import settings

from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework import mixins
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated

ALLOWED_HOSTS = settings.ALLOWED_HOSTS


class GenericClientAPIView(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, mixins.RetrieveModelMixin):
    serializer_class = ClientSerializer
    queryset = Client.objects.all()
    lookup_field = 'id'
    # authentication_classes = [SessionAuthentication, BasicAuthentication]
    # permission_classes = [IsAuthenticated]

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
        return self.update(request, id)

    def delete(self, request, id):
        return self.destroy(request, id)


class ClientAPIView(APIView):
    def get(self, request):
        clients = Client.objects.all()
        serializer = ClientSerializer(clients, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ClientSerializer(data=request.POST)
        next_url = request.POST.get('next')
        if serializer.is_valid():
            serializer.save()
            if next_url != None and is_safe_url(next_url, ALLOWED_HOSTS):
                return Response(serializer.data, status=status.HTTP_201_CREATED) and redirect(next_url)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ClientDetails(APIView):

    def get_object(self, id):
        try:
            return Client.objects.get(pk=id)
        except Client.DoesNotExist:
            return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    def get(self, request, id):
        client = self.get_object(id)
        serializer = ClientSerializer(client)
        return Response(serializer.data)

    def put(self, request, id):
        client = self.get_object(id)
        serializer = ClientSerializer(client, data=request.data)
        if request.POST.get('next') != '':
            next_url = request.POST.get('next')
        else:
            next_url = None
        if serializer.is_valid():
            serializer.save()
            if next_url != None and is_safe_url(next_url, ALLOWED_HOSTS):
                return Response(serializer.data, status=status.HTTP_201_CREATED) and redirect(next_url)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        client = self.get_object(id)
        client.delete()
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)


@ api_view(['GET', 'POST'])
def client_list(request):
    if request.method == 'GET':
        clients = Client.objects.all()
        serializer = ClientSerializer(clients, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ClientSerializer(data=request.POST)
        next_url = request.POST.get('next')
        if serializer.is_valid():
            serializer.save()
            if next_url != None and is_safe_url(next_url, ALLOWED_HOSTS):
                return Response(serializer.data, status=status.HTTP_201_CREATED) and redirect(next_url)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@ api_view(['GET', 'PUT', 'DELETE'])
def client_detail(request, pk):
    try:
        client = Client.objects.get(pk=pk)
    except Client.DoesNotExist:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ClientSerializer(client)
        return Response(serializer.data)

    elif request.method == 'PUT':
        # data = JSONParser().parse(request)
        serializer = ClientSerializer(client, data=request.data)
        if request.POST.get('next') != '':
            next_url = request.POST.get('next')
        else:
            next_url = None
        if serializer.is_valid():
            serializer.save()
            if next_url != None and is_safe_url(next_url, ALLOWED_HOSTS):
                return Response(serializer.data, status=status.HTTP_201_CREATED) and redirect(next_url)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        client.delete()
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)
