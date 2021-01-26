from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from django.urls import reverse
from django.utils.safestring import mark_safe


class SellerRegistration(models.Model):
    Name = models.CharField(max_length=50)
    ShopName = models.CharField(max_length=50, unique=True, verbose_name='Shop Name')
    ShopLogo = models.ImageField(upload_to='Photos', verbose_name='Shop Logo')
    Phone = models.CharField(max_length=15)
    Email = models.EmailField(unique=True)
    Address = models.TextField(unique=True)
    NID = models.CharField(max_length=50, unique=True)
    TradeLicense = models.CharField(max_length=50, unique=True, verbose_name='Trade License')
    NIDImage = models.ImageField(upload_to='Photos', verbose_name='NID Image')
    TradeImage = models.ImageField(upload_to='Photos', verbose_name='Trade License Image')

    def __str__(self):
        return self.ShopName

    def Shop_Logo(self):
        return mark_safe('<img src="{}" width="70" height ="70" />'.format(self.ShopLogo.url))

    Shop_Logo.short_description = 'Image'
    Shop_Logo.allow_tags = True


class sellerProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    ShopDetails = models.OneToOneField(SellerRegistration, on_delete=models.CASCADE, null=True)
    isSeller = models.BooleanField(default=False)

    def __str__(self):
        return self.ShopDetails.ShopName

    def get_absolute_url(self):
        return reverse("sellerProfile.html", kwargs={'slug': self.slug})
