from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField, UserCreationForm
from django.db.models.fields import TextField
from django.forms import widgets
from django.forms.fields import EmailField

from user_account.models import User


class CreateProfileForm(forms.Form):
    first_name = forms.CharField(max_length=150)
    last_name = forms.CharField(max_length=150)
    email = EmailField()
    profile_picture = forms.ImageField(required=False)
    bio = forms.CharField(widget=forms.Textarea)

class RegisterForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ("email",)



class LoginForm(forms.Form):
    username = forms.CharField(max_length=150)
    password = forms.CharField(widget=forms.PasswordInput)


class RegisterForm(forms.Form):
    username = forms.CharField(max_length=150)
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)


