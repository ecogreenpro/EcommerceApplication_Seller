from django import template
from django.utils.safestring import mark_safe

from core.models import CartProducts, Order, Shipping

register = template.Library()


@register.simple_tag
def checkout_li():
    items = CartProducts.objects.filter(isOrdered=False)
    items_li = ""
    for i in items:
        items_li += """<tr start="1">
     <li class="list-group-item d-flex justify-content-between lh-condensed">
        <div>
             <h6 class="my-0">{}</h6>
             <small class="text-muted">Brief description</small>
         </div>
        <span class="text-muted">{}</span>
     </li>
         """.format(
            i.item.name, i.get_final_price())
    return mark_safe(items_li)


@register.simple_tag
def shipping_li():
    items = Shipping.objects.filter(isActive=True)
    shipping_li = ""
    for i in items:
        shipping_li += """
              <li class="list-group-item d-flex justify-content-between lh-condensed">
                                    <div>
                                        <h6 class="my-0">Shipping <small class="text-muted">({})</small></h6>

                                    </div>
                                    <span class="text-muted">{}</span>
                                </li>               
         """.format(
            i.location, i.charge)
    return mark_safe(shipping_li)
