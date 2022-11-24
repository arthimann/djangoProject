from django import forms
from .models import MemberModel
from django.contrib.auth.forms import UserCreationForm


class LoginForm(forms.ModelForm):
    username = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = MemberModel
        fields = ['username', 'password']


class UserRegistrationForm(UserCreationForm):
    username = forms.CharField(
        max_length=255,
        widget=forms.TextInput(
            attrs={'class': 'form-control'}
        )
    )
    password1 = forms.CharField(
        max_length=255,
        label='Password',
        widget=forms.TextInput(
            attrs={'class': 'form-control'}
        )
    )
    password2 = forms.CharField(
        max_length=255,
        label='Re-Password',
        widget=forms.TextInput(
            attrs={'class': 'form-control'}
        )
    )
