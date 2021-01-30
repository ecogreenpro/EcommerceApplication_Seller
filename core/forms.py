from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from django.forms import TextInput, EmailInput, Select, FileInput

from .models import userProfile


class RegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2', ]


class ProfileModelForm(forms.ModelForm):
    class Meta:
        model = userProfile
        fields = ['address', 'image', 'country', 'city', 'Phone']




class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = userProfile
        fields = ('Phone', 'address', 'city', 'country', 'image')
        widgets = {
            'Phone': TextInput(attrs={'class': 'input', 'placeholder': 'Phone'}),
            'address': TextInput(attrs={'class': 'input', 'placeholder': 'address'}),
            'city': TextInput(attrs={'class': 'input', 'placeholder': 'city'}),
            'country': TextInput(attrs={'class': 'input', 'placeholder': 'country'}),
            'image': FileInput(attrs={'class': 'input', 'placeholder': 'image', }),
        }
