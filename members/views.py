from django.shortcuts import render, redirect
from .forms import LoginForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import UserRegistrationForm


def login_view(request, *args, **kwargs):
    form = LoginForm(request.POST or None)

    if request.method == 'POST':
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            messages.success(request, 'User not found')

    return render(request, 'members/login.html', {
        'form': form
    })


def logout_view(request, *args, **kwargs):
    logout(request)
    return redirect('members')


def register_view(request, *args, **kwargs):
    form = UserRegistrationForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('/')
    return render(request, 'members/register.html', {
        'form': form
    })
