from .models import ContactRequest
from django import forms


class ContactForm(forms.ModelForm):
    """
    Form to allow signed in users to leave a request for contact
    """
    class Meta:
        model = ContactRequest
        fields = ('name', 'email', 'message')