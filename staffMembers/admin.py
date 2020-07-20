from django.contrib import admin
from .models import StaffMember


class StaffMemberAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'name', 'position', 'contactNumber']


admin.site.register(StaffMember, StaffMemberAdmin)
