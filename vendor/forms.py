from ckeditor.widgets import CKEditorWidget
from django import forms
from django.contrib.auth.forms import UserChangeForm
from django.forms import TextInput, EmailInput, FileInput
from core.models import Products, OrderProduct, Order
from .models import *


class SellerRegistrationForm(forms.ModelForm):
    class Meta:
        model = SellerRegistration
        fields = ['Name', 'ShopName', 'ShopLogo', 'Phone', 'Email', 'Address', 'NID', 'TradeLicense', 'NIDImage',
                  'TradeImage']

        widgets = {
            'Name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your Name'}),
            'ShopName': forms.TextInput(attrs={'class': 'form-control'}),
            'ShopLogo': forms.FileInput(attrs={'required': True, }),
            'Phone': forms.NumberInput(attrs={'class': 'form-control'}),
            'Email': forms.EmailInput(attrs={'class': 'form-control'}),
            'Address': forms.Textarea(attrs={'class': 'form-control'}),
            'NID': forms.NumberInput(attrs={'class': 'form-control'}),
            'TradeLicense': forms.NumberInput(attrs={'class': 'form-control'}),
            'NIDImage': forms.FileInput(attrs={'required': True, }),
            'TradeImage': forms.FileInput(attrs={'required': True, }),

        }


class AddProductForm(forms.ModelForm):
    shortDescription = forms.CharField(widget=CKEditorWidget()),
    longDescirption = forms.CharField(widget=CKEditorWidget()),

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop("request")
        super(AddProductForm, self).__init__(*args, **kwargs)
        self.fields['user'].initial = self.request.user

    class Meta:
        model = Products
        fields = ['user', 'name', 'slug', 'price', 'discountPrice', 'category', 'brand', 'label', 'stockQuantity',
                  'shortDescription', 'longDescirption', 'mainImage', 'altImageOne', 'altImageTwo']
        widgets = {
            'user': forms.HiddenInput(),
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'slug': forms.TextInput(attrs={'class': 'form-control'}),
            'price': forms.NumberInput(attrs={'class': 'form-control'}),
            'discountPrice': forms.NumberInput(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
            'brand': forms.Select(attrs={'class': 'form-control'}),
            'label': forms.Select(attrs={'class': 'form-control'}),
            'stockQuantity': forms.NumberInput(attrs={'class': 'form-control'}),
            'mainImage': forms.FileInput(attrs={'required': True, }),
            'altImageOne': forms.FileInput(attrs={'required': True, }),
            'altImageTwo': forms.FileInput(attrs={'required': True, })

        }


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = SellerRegistration
        fields = ('Name', 'ShopName', 'Phone', 'Email', 'Address', 'ShopLogo',)
        widgets = {
            'Name': TextInput(attrs={'class': 'form-control', 'placeholder': 'Name'}),
            'ShopName': TextInput(attrs={'class': 'form-control', 'placeholder': 'Shop Name'}),
            'Phone': TextInput(attrs={'class': 'form-control', 'placeholder': 'Phone'}),
            'Email': EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
            'Address': TextInput(attrs={'class': 'form-control', 'placeholder': 'Address'}),
            'ShopLogo': forms.FileInput(attrs={'required': True, }),
        }


class updateForm(forms.ModelForm):
    shortDescription = forms.CharField(widget=CKEditorWidget()),
    longDescirption = forms.CharField(widget=CKEditorWidget()),

    class Meta:
        model = Products
        fields = ['user', 'name', 'slug', 'price', 'discountPrice', 'category', 'brand', 'label', 'stockQuantity',
                  'shortDescription', 'longDescirption', 'mainImage', 'altImageOne', 'altImageTwo']
        widgets = {
            'user': forms.HiddenInput(),
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'slug': forms.TextInput(attrs={'class': 'form-control'}),
            'price': forms.NumberInput(attrs={'class': 'form-control'}),
            'discountPrice': forms.NumberInput(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
            'brand': forms.Select(attrs={'class': 'form-control'}),
            'label': forms.Select(attrs={'class': 'form-control'}),
            'stockQuantity': forms.NumberInput(attrs={'class': 'form-control'}),
            'mainImage': forms.FileInput(attrs={'required': True, }),
            'altImageOne': forms.FileInput(attrs={'required': True, }),
            'altImageTwo': forms.FileInput(attrs={'required': True, })

        }
