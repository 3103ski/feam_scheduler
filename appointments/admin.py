from django.contrib import admin

from .models import Appointment

# ======================
#   Admin Class
# ======================


class AppointmentAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'createdBy', 'notes']
    search_fields = ['client', 'user__username', 'user__email']


admin.site.register(Appointment, AppointmentAdmin)
