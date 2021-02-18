from django import template
from django.utils.safestring import mark_safe

from vendor.models import SellerRegistration

register = template.Library()


@register.simple_tag
def sellerCount(id):
    count = SellerRegistration.objects.filter(id=id).count()
    return count

