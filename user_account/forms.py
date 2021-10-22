from django import forms
from django.db.models.fields import TextField
from django.forms.fields import EmailField


class LoginForm(forms.Form):
    email = EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
    

class RegisterForm(forms.Form):
    first_name = forms.CharField(max_length=150)
    last_name = forms.CharField(max_length=150)
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)


class EditAccountForm(forms.Form):
    first_name = forms.CharField(max_length=150)
    last_name = forms.CharField(max_length=150)
    email = forms.EmailField()
    picture = forms.ImageField(required=False)
    bio = forms.CharField(widget=forms.Textarea)
    password = forms.CharField(widget=forms.PasswordInput)
