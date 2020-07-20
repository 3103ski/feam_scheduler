from django.contrib import admin
from .models import DaySchedule


class DayScheduleAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'briefingTime', 'reminders', 'date']


admin.site.register(DaySchedule, DayScheduleAdmin)
