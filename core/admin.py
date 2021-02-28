from django.contrib import admin
from .models import Categories, Brands, Products, CartProducts, Order, Coupon, userProfile, Shipping, OrderProduct, \
    Settings, CarouselAdvImage, Balance


class CategoriesAdmin(admin.ModelAdmin):
    list_display = [
        'Catagories_photo',
        'name',
        'slug',
        'description',
        'isactive'
    ]
    list_display_links = ['Catagories_photo', 'name']
    prepopulated_fields = {'slug': ("name",)}
    list_filter = ['name', 'isactive']
    search_fields = ['name', 'isactive']


class BrandsAdmin(admin.ModelAdmin):
    list_display = [
        'brands_photo',
        'name',
        'slug',
        'description',
        'isactive'
    ]
    list_display_links = ['brands_photo', 'name']
    prepopulated_fields = {'slug': ("name",)}
    list_filter = ['name', 'isactive']
    search_fields = ['name']


class ProductsAdmin(admin.ModelAdmin):
    list_display = [
        'products_photo',
        'name',
        'slug',
        'price',
        'discountPrice',
        'label',
        'stockQuantity',
        'shortDescription',
        'isactive'
    ]
    list_display_links = ['products_photo', 'name']
    prepopulated_fields = {'slug': ("name",)}
    list_filter = ['name', 'isactive', 'category']
    search_fields = ['name']


class CartProductsAdmin(admin.ModelAdmin):
    list_display = [
        'user',
        'item',
        'quantity'
    ]





class ShippingAdmin(admin.ModelAdmin):
    list_display = [
        'location',
        'charge',

    ]


class OrderProductAdmin(admin.ModelAdmin):
    list_display = ['user', 'product', 'price', 'quantity', 'amount']
    list_filter = ['user']


class OrderProductline(admin.TabularInline):
    model = OrderProduct
    readonly_fields = ('user', 'product', 'price', 'quantity', 'amount')
    can_delete = True
    extra = 0


class OderAdmin(admin.ModelAdmin):
    list_display = [
        'first_name',
        'order_Number',
        'phone_number',
        'address',
        'ordered_date',
        'OrderTotal',
        'order_status',

    ]
    search_fields = ['order_Number', 'phone_number']
    inlines = [OrderProductline]


class userProfileAdmin(admin.ModelAdmin):
    list_display = [
        'userPhoto',
        'user',
        'slug',
        'address',
        'Phone',
        'isActive'
    ]
    list_display_links = ['userPhoto', 'user']
    prepopulated_fields = {'slug': ("user",)}
    list_filter = ['user', 'isActive']
    search_fields = ['Phone',]



class settingsAdmin(admin.ModelAdmin):
    list_display = [
        'SiteLogo',
        'siteTitle',
        'address',
        'phone',
        'isActive'
    ]


class CarouselAdvImageAdmin(admin.ModelAdmin):
    list_display = [
        'title',
        'Home_carousel1',
        'Home_Adv_Bottom_long',
        'Shop_carousel1',

    ]

class BalanceAdmin(admin.ModelAdmin):
    list_display = [
        'user',
        'points'
    ]
    search_fields = ['user']

admin.site.register(CarouselAdvImage, CarouselAdvImageAdmin)
admin.site.register(Settings, settingsAdmin)
admin.site.register(Categories, CategoriesAdmin)
admin.site.register(Brands, BrandsAdmin)
admin.site.register(Products, ProductsAdmin)
admin.site.register(CartProducts, CartProductsAdmin)
admin.site.register(Shipping, ShippingAdmin)
admin.site.register(Order, OderAdmin)
admin.site.register(OrderProduct, OrderProductAdmin)
admin.site.register(userProfile, userProfileAdmin)
admin.site.register(Balance, BalanceAdmin)
