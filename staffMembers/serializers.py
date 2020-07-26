from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import StaffMember


class StaffMemberSerializer(serializers.ModelSerializer):
    def clean_name(self):
        name = self.cleaned_data.get('name')
        return name

    class Meta:
        model = StaffMember
        fields = ['name', 'position', 'createdBy', 'createdOn', 'lastModified',
                  'contactNumber', 'emailAddress', 'team', 'supervisor']
