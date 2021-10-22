from django import forms

class CreateMessageForm(forms.Form):
    message = forms.CharField(widget=forms.Textarea())