from django import forms
from .models import Message

class CreateMessageForm(forms.Form):
    message = forms.CharField(widget=forms.Textarea())