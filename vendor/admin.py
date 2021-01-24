from django.contrib import admin
from .models import sellerProfile, SellerRegistration


# Register your models here.
class BecomeSellerline(admin.TabularInline):
    model = sellerProfile
    fields = ('ShopDetails', 'user','isSeller')
    can_delete = True
    extra = 0


class SellerProfileAdmin(admin.ModelAdmin):
    list_display = [

        'ShopDetails',
        'user',
        'isSeller'
    ]

    list_filter = ['user']
    search_fields = ['ShopDetails']



admin.site.register(sellerProfile, SellerProfileAdmin)


class BecomeSellerAdmin(admin.ModelAdmin):
    list_display = [

        'Shop_Logo',
        'ShopName',
        'Address',
        'Phone',
        'NID',
        'TradeLicense'
    ]

    list_filter = ['NID']
    search_fields = ['ShopName']
    inlines = [BecomeSellerline]

admin.site.register(SellerRegistration, BecomeSellerAdmin)
