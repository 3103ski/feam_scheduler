from rest_framework import serializers
from .models import Client
from django.contrib.auth import get_user_model

User = get_user_model()


def get_sentinel_user():
    return get_user_model().objects.get_or_create(username='deleted')[0]


class ClientSerializer(serializers.ModelSerializer):

    def clean_name(self):
        name = self.cleaned_data.get('name')
        return name

    class Meta:
        model = Client
        fields = ['name', 'clientNotes', 'address', 'contactNumber',
                  'createdBy', 'createdOn', 'lastModified', 'id']
