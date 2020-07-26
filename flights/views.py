from django.shortcuts import render
from .models import Flight
from .serializers import FlightSerializer
from django.shortcuts import redirect
from django.utils.http import is_safe_url
from django.conf import settings

from rest_framework import generics
from rest_framework import mixins
# from rest_framework.authentication import SessionAuthentication, BasicAuthentication
# from rest_framework.permissions import IsAuthenticated

# from .forms import FlightForm
# from django.shortcuts import render, redirect
# from django.http import HttpResponse, Http404, JsonResponse
# from rest_framework.response import Response
# from rest_framework.authentication import SessionAuthentication
# from rest_framework.decorators import api_view, permission_classes, authentication_classes
# from rest_framework.permissions import IsAuthenticated


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


# def flight_list(request):
#     if request.method == 'GET':
#         flights = Flight.objects.all()
#         serializer = FlightSerializer(flights, many=True)
#         return JsonResponse(serializer.data, safe=False)

#     elif request.method == 'POST':
#         serializer = FlightSerializer(data=request.POST)
#         next_url = request.POST.get('next')
#         if serializer.is_valid():
#             serializer.save()
#             if next_url != None and is_safe_url(next_url, ALLOWED_HOSTS):
#                 return JsonResponse(serializer.data, status=201) and redirect(next_url)
#             return JsonResponse(serializer.data, status=201)
#         return JsonResponse(serializer.errors, status=400)


# def flight_detail(request, pk):
#     try:
#         flight = Flight.objects.get(pk=pk)
#     except Flight.DoesNotExist:
#         return HttpResponse(status=404)

#     if request.method == 'GET':
#         serializer = FlightSerializer(flight)
#         return JsonResponse(serializer.data)

#     elif request.method == 'PUT':
#         data = JSONParser().parse(request)
#         serializer = FlightSerializer(article, data=data)
#         if serializer.is_valid():
#             serializer.save()
#             if next_url != None and is_safe_url(next_url, ALLOWED_HOSTS):
#                 return JsonResponse(serializer.data, status=201) and redirect(next_url)
#             return JsonResponse(serializer.data, status=201)
#         return JsonResponse(serializer.errors, status=400)

#     elif request.method == 'DELETE':
#         flight.delete()
#         return HttpResponse(status=204)


# def flight_action(request):
#     print(request.data)
#     # action = request.data.action
#     # flight_id = request.data.id

#     # if action == 'delete':
#     #     Flight.objects.delete(id=flight_id)
#     return redirect('/flights/')
