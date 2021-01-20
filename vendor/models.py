from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class SellerRegistration(models.Model):
    Name = models.CharField(max_length=50)
    CompanyName = models.CharField(max_length=50, unique=True, verbose_name='Company Name')
    Phone = models.CharField(max_length=15)
    Email = models.EmailField()
    Address = models.TextField()
    NID = models.CharField(max_length=50)
    TradeLicense = models.CharField(max_length=50, verbose_name='Trade License')
    NIDImage = models.ImageField(upload_to='Photos', verbose_name='NID Image')
    TradeImage = models.ImageField(upload_to='Photos', verbose_name='Trade License Image')

    def __str__(self):
        return self.CompanyName


class sellerProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    CompanyName = models.CharField(max_length=50, unique=True, verbose_name='Company Name')
    Address = models.TextField()
    Phone = models.CharField(max_length=20, default="+8801xxxxxxxxx", null=False)
    NID = models.CharField(max_length=50, unique=True)
    TradeLicense = models.CharField(max_length=50, verbose_name='Trade License', unique=True)
    NIDImage = models.ImageField(upload_to='Photos', verbose_name='NID Image')
    TradeImage = models.ImageField(upload_to='Photos', verbose_name='Trade License Image')
    isSeller = models.BooleanField(default=False)

    def __str__(self):
        return self.CompanyName

    def get_absolute_url(self):
        return reverse("sellerProfile", kwargs={'slug': self.slug})

    def sellerPhoto(self):
        return mark_safe('<img src="{}" width="70" height ="70" />'.format(self.image.url))

    sellerPhoto.short_description = 'Image'
    sellerPhoto.allow_tags = True
