from django import forms
from .models import Client


class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ['name', 'clientNotes', 'address', 'contactNumber']

    def clean_clientNotes(self):
        clientNotes = self.cleaned_data.get('clientNotes')

        return clientNotes
