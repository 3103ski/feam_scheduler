from django.contrib import admin
from .models import Client


class ClientAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'createdBy', 'createdOn', 'lastModified']
    search_fields = ['name', 'createdBy', 'user__username', 'user__email']


admin.site.register(Client, ClientAdmin)
