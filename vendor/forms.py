from django import forms
from .models import *


class SellerRegistrationForm(forms.ModelForm):
    class Meta:
        model = SellerRegistration
        fields = ['Name', 'CompanyName', 'Phone', 'Email', 'Address', 'NID', 'TradeLicense', 'NIDImage', 'TradeImage']

        widgets = {
            'Name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your Name'}),
            'CompanyName': forms.TextInput(attrs={'class': 'form-control'}),
            'Phone': forms.NumberInput(attrs={'class': 'form-control'}),
            'Email': forms.EmailInput(attrs={'class': 'form-control'}),
            'Address': forms.Textarea(attrs={'class': 'form-control'}),
            'NID': forms.NumberInput(attrs={'class': 'form-control'}),
            'TradeLicense': forms.NumberInput(attrs={'class': 'form-control'}),
            'NIDImage': forms.FileInput(attrs={'required': True, }),
            'TradeImage': forms.FileInput(attrs={'required': True, }),

        }
