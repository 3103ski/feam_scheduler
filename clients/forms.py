from django import forms
from .models import Client


class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ['name', 'clientDescription', 'address', 'phoneNumber']

    def clean_clientDescription(self):
        # collect form data
        clientDescription = self.cleaned_data.get('clientDescription')

        # check description length
        if len(clientDescription) > 300:
            raise forms.ValidationError(
                "Please describe the company in less than 300 characters.")

        return clientDescription
