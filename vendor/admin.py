from django.contrib import admin
from .models import sellerProfile, SellerRegistration


# Register your models here.
class SellerRegistrationAdmin(admin.ModelAdmin):
    list_display = [

        'ShopName',
        'Phone',
        'NID',
        'TradeLicense',
        'isSeller'
    ]

    list_filter = ['NID']
    search_fields = ['ShopName']


admin.site.register(sellerProfile, SellerRegistrationAdmin)


class BecomeSellerAdmin(admin.ModelAdmin):
    list_display = [

        'ShopName',
        'Phone',
        'NID',
        'TradeLicense'
    ]

    list_filter = ['NID']
    search_fields = ['ShopName']


admin.site.register(SellerRegistration, BecomeSellerAdmin)
