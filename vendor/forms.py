from django import forms

from core.models import Products
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
            'shortDescription': forms.Textarea(attrs={'class': 'form-control'}),
            'longDescirption': forms.Textarea(attrs={'class': 'form-control'}),
            'mainImage': forms.FileInput(attrs={'required': True, }),
            'altImageOne': forms.FileInput(attrs={'required': True, }),
            'altImageTwo': forms.FileInput(attrs={'required': True, })

        }
