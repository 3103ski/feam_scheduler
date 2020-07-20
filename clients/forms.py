from django import forms
from .models import Client


class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ['name', 'clientNotes', 'address', 'contactNumber']

    def clean_clientNotes(self):
        # collect form data
        clientNotes = self.cleaned_data.get('clientNotes')

        # check description length
        if len(clientDescription) > 300:
            raise forms.ValidationError(
                "Please describe the company in less than 300 characters.")

        return clientNotes
