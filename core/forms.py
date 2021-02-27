from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from django.forms import TextInput, EmailInput, Select, FileInput
from django_simple_coupons.models import Coupon

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
            'Phone': TextInput(attrs={'class': 'form-control', 'placeholder': 'Phone'}),
            'address': TextInput(attrs={'class': 'form-control', 'placeholder': 'address'}),
            'city': TextInput(attrs={'class': 'form-control', 'placeholder': 'city'}),
            'country': Select(attrs={'class': 'form-control', 'placeholder': 'country'}),
            'image': FileInput(attrs={'class': '', 'placeholder': 'image', }),
        }


class CouponApplyForm(forms.Form):
    code = forms.CharField()
