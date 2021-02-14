from django.db import models
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.forms import EmailField
from django.shortcuts import reverse
from django.utils.safestring import mark_safe
from django_countries.fields import CountryField
from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.auth.models import User
from django.db.models import Count

Label_Choices = (
    ('Sale', 'Sale'),
    ('New', 'New'),
    ('Flash Sale', 'Flash Sale'),
    ('Promotion', 'Promotion')
)
Payment_Choices = (
    ('Cash On Delivery', 'Cash on Delivery'),
    ('Bkash', 'Bkash')
)

Status_Choices = (

    ('Processing', 'Processing'),
    ('Pending', 'Pending'),
    ('Canceled', 'Canceled'),
    ('Delivered', 'Delivered'),
    ('Refund in Process', 'Refund in Process'),
    ('Refunded', 'Refunded')

)


class Categories(models.Model):
    name = models.CharField(max_length=100, unique=True)
    icon = models.ImageField(upload_to='Photos')
    slug = models.SlugField(unique=True)
    description = RichTextUploadingField()
    image = models.ImageField(upload_to='Photos')
    isactive = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("core:categories", kwargs={'slug': self.slug})

    def Catagories_photo(self):
        return mark_safe('<img src="{}" width="70" height ="70" />'.format(self.image.url))

    Catagories_photo.short_description = 'Image'
    Catagories_photo.allow_tags = True


class Brands(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(unique=True)
    description = RichTextUploadingField()
    image = models.ImageField(upload_to='Photos')
    isactive = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("core:brands", kwargs={'slug': self.slug})

    def brands_photo(self):
        return mark_safe('<img src="{}" width="70" height ="70" />'.format(self.image.url))

    brands_photo.short_description = 'Image'
    brands_photo.allow_tags = True


class Products(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    price = models.FloatField()
    discountPrice = models.FloatField(blank=True, null=True, verbose_name="Discount Price")
    category = models.ForeignKey(Categories, on_delete=models.CASCADE)
    brand = models.ForeignKey(Brands, on_delete=models.CASCADE, null=True)
    label = models.CharField(choices=Label_Choices, max_length=30)
    stockQuantity = models.IntegerField(default=1, verbose_name="Stock Quantity")
    shortDescription = RichTextUploadingField()
    longDescirption = RichTextUploadingField()
    mainImage = models.ImageField(upload_to='Photos', verbose_name="Main Image")
    altImageOne = models.ImageField(upload_to='Photos', verbose_name="Gallery Image One")
    altImageTwo = models.ImageField(upload_to='Photos', verbose_name="Gallery Image Two")
    isactive = models.BooleanField(default=False, verbose_name="Is Active")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("core:product", kwargs={'slug': self.slug})

    def get_add_to_cart_url(self):
        return reverse("core:add-to-cart", kwargs={
            'slug': self.slug
        })

    def get_remove_from_cart_url(self):
        return reverse("core:remove-from-cart", kwargs={
            'slug': self.slug
        })

    def products_photo(self):
        return mark_safe('<img src="{}" width="70" height ="70" />'.format(self.mainImage.url))

    def get_percentage(self):
        if self.discountPrice:
            discount = (100 * ((self.price - self.discountPrice) / self.price))
            return discount.__int__()
        else:
            return self.price

    products_photo.short_description = 'Image'
    products_photo.allow_tags = True


class CartProducts(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    isOrdered = models.BooleanField(default=False)
    item = models.ForeignKey(Products, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.quantity} of {self.item.name}"

    def get_total_product_price(self):
        return self.quantity * self.item.price

    def get_total_discount_product_price(self):
        return self.quantity * self.item.discountPrice

    def get_amount_saved(self):
        return self.get_total_product_price() - self.get_total_discount_product_price()

    @property
    def get_final_price(self):
        if self.item.discountPrice:
            return self.get_total_discount_product_price()
        return self.get_total_product_price()

    def price(self):
        if self.item.discountPrice:
            return self.item.discountPrice
        else:
            return self.item.price

    def get_total(self):
        total = 0
        for order_item in self:
            total += order_item.get_final_price()

        return total


class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    order_Number = models.CharField(max_length=20, null=True)
    first_name = models.CharField(max_length=30, null=True)
    last_name = models.CharField(max_length=30, null=True)
    phone_number = models.CharField(max_length=30, null=True)
    email = models.EmailField(null=True)
    ordered_date = models.DateTimeField(auto_now_add=True, null=True)
    address = models.CharField(max_length=100, null=True)
    country = models.CharField(max_length=30, null=True)
    district = models.CharField(max_length=30, null=True)
    zip_code = models.CharField(max_length=10, null=True)
    order_note = models.TextField(max_length=70, null=True)

    payment = models.CharField(choices=Payment_Choices, max_length=20, null=True)
    coupon = models.ForeignKey(
        'Coupon', on_delete=models.SET_NULL, blank=True, null=True)
    shipping = models.ForeignKey(
        'Shipping', on_delete=models.SET_NULL, blank=True, null=True)
    order_status = models.CharField(choices=Status_Choices, max_length=20, null=True)
    OrderTotal = models.FloatField(blank=True, null=True)

    def __str__(self):
        return self.order_Number


class OrderProduct(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    product = models.ForeignKey(Products, on_delete=models.CASCADE, null=True)
    quantity = models.IntegerField(null=True)
    price = models.FloatField(null=True)
    amount = models.FloatField(null=True)
    create_at = models.DateTimeField(auto_now_add=True, null=True)
    update_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.product.name

    def get_total(self):
        total = 0
        for order_item in self.product.all():
            total += order_item.get_final_price()

        return total


class Coupon(models.Model):
    code = models.CharField(max_length=15)
    amount = models.FloatField()

    def __str__(self):
        return self.code


class Shipping(models.Model):
    location = models.CharField(max_length=30)
    charge = models.FloatField()
    isActive = models.BooleanField(default=True)

    def __str__(self):
        return self.location


class userProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    slug = models.SlugField(unique=True, null=True)
    address = models.TextField(null=True)
    image = models.ImageField(upload_to='Photos', default='avatar.png')
    country = CountryField(blank_label='(Select Country)', null=True)
    city = models.CharField(max_length=30, null=True)
    Phone = models.CharField(max_length=20, null=True)
    isActive = models.BooleanField(default=True)

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            userProfile.objects.create(user=instance)

    def __str__(self):
        return self.user.first_name

    def get_absolute_url(self):
        return reverse("core:categories", kwargs={'slug': self.slug})

    def userPhoto(self):
        return mark_safe('<img src="{}" width="70" height ="70" />'.format(self.image.url))

    userPhoto.short_description = 'Image'
    userPhoto.allow_tags = True


class Settings(models.Model):
    siteTitle = models.CharField(max_length=150)
    description = models.CharField(max_length=255)
    address = models.CharField(blank=True, max_length=100)
    phone = models.CharField(blank=True, max_length=15)
    email = models.CharField(blank=True, max_length=50)
    logo = models.ImageField(blank=True, upload_to='Photos')
    favIcon = models.ImageField(blank=True, upload_to='Photos')
    facebook = models.CharField(blank=True, max_length=50)
    instagram = models.CharField(blank=True, max_length=50)
    twitter = models.CharField(blank=True, max_length=50)
    youtube = models.CharField(blank=True, max_length=50)
    aboutus = RichTextUploadingField(blank=True)
    privacyPolicy = RichTextUploadingField(blank=True)
    returnPolicy = RichTextUploadingField(blank=True)
    paymentProcess = RichTextUploadingField(blank=True)
    contact = RichTextUploadingField(blank=True)
    isActive = models.BooleanField(max_length=10, default=False)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.siteTitle

    def SiteLogo(self):
        return mark_safe('<img src="{}" width="70" height ="70" />'.format(self.logo.url))

    SiteLogo.short_description = 'Image'
    SiteLogo.allow_tags = True


class CarouselAdvImage(models.Model):
    title = models.CharField(max_length=50, blank=True)
    Home_carousel1 = models.ImageField(blank=True, upload_to='Photos')
    Home_carousel2 = models.ImageField(blank=True, upload_to='Photos')
    Home_carousel3 = models.ImageField(blank=True, upload_to='Photos')
    Home_Adv_top1 = models.ImageField(blank=True, upload_to='Photos')
    Home_Adv_top2 = models.ImageField(blank=True, upload_to='Photos')
    Home_Adv_middle1 = models.ImageField(blank=True, upload_to='Photos')
    Home_Adv_middle2 = models.ImageField(blank=True, upload_to='Photos')
    Home_Adv_middle3 = models.ImageField(blank=True, upload_to='Photos')
    Home_Adv_Bottom_long = models.ImageField(blank=True, upload_to='Photos')
    Home_Adv_Bottom_Short = models.ImageField(blank=True, upload_to='Photos')
    Shop_carousel1 = models.ImageField(blank=True, upload_to='Photos')
    Shop_carousel2 = models.ImageField(blank=True, upload_to='Photos')
    Shop_carousel3 = models.ImageField(blank=True, upload_to='Photos')
    Become_Seller_Image = models.ImageField(blank=True, upload_to='Photos')

    def __str__(self):
        return self.title
