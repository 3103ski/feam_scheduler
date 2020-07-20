from django.contrib import admin
from .models import Flight


class FlightAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'flightNumber', 'tailNumber', 'scheduledTOA']


admin.site.register(Flight, FlightAdmin)
