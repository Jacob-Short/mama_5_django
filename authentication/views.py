from django.shortcuts import render, HttpResponseRedirect, reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.conf import settings
from django import forms
from authentication.models import MyUser
from authentication.forms import LoginForm
from authentication.models import MyUser


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(
                username=data['username'],
                password=data['password'],
            )
            if user:
                login(request, user)
                context = {}
                return HttpResponseRedirect(reverse('home'))
    form = LoginForm()
    context = {'form': form}
    return render(request, 'generic_form.html', context)