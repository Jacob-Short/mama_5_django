from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField, UserCreationForm
from django.db.models.fields import TextField
from django.forms.fields import EmailField

from user_account.models import User




class RegisterForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ("email",)



class LoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)


class RegisterForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)


class UserEditForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = User
        fields = (
            "email",
            "first_name",
            "last_name",
            "picture",
            "bio",
            "password",
            "is_active",
        )