from django.contrib import admin

from .models import Appointment

# ======================
#   Admin Class
# ======================


class AppointmentAdmin(admin.ModelAdmin):
    list_display = ['__str__',  'appointmentTime',
                    'appointmentDate',  'appointmentNotes', 'lastModified']
    search_fields = ['appointmentDate', 'appointmentTime', 'client',
                     'user__username', 'user__email']


admin.site.register(Appointment, AppointmentAdmin)
