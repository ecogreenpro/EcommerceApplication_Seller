from django import template
from django.utils.safestring import mark_safe

from core.models import CartProducts, Order, Products, Shipping

register = template.Library()


@register.simple_tag
def cartCount(userid):
    count = CartProducts.objects.filter(user_id=userid).count()
    return count


@register.simple_tag
def prductCount():
    count = Products.objects.all().count()
    return count


@register.simple_tag
def cartTotal(userid):
    cart = CartProducts.objects.filter(user_id=userid)
    total = 0
    for rs in cart:
        if rs.item.discountPrice:
            total += rs.item.discountPrice * rs.quantity
        else:
            total += rs.item.price * rs.quantity
    return total


@register.simple_tag
def cartPage_li():
    items = CartProducts.objects.filter(isOrdered=False)
    items_li = ""
    for i in items:
        items_li += """<tr start="1">
        <td>#</td>
        <td width="20%">
            <div class="display-flex">
                 <div class="img-product">
                    <img src="/media/{}" alt="" >
                 </div>
            </div>
        </td>
         <td>{}</td>
         <td width="10%" class="text-center">{}</td>
         <td width="10%" class="text-center"><a href= "#" class="trash-icon "><i class="fas fa-minus mr-3"></i></a>{} 
         <a href= "#" class="trash-icon "><i class="fas fa-plus ml-3"></i></a>
         </td>
         <td width="10%" class="text-center">{}</td>
         <td width="10%" class="text-center ">
            <a href="#" class="trash-icon "><i class="far fa-trash-alt "></i></a>
            </td>
         </tr>
         """.format(
            i.item.mainImage, i.item.name, i.price(), i.quantity, i.get_final_price())
    return mark_safe(items_li)


@register.simple_tag
def cartPage_total():
    items = Order.objects.filter(isOrdered=False)
    items_li = ""
    for i in items:
        items_li += """<tr start="1">
         <td>{}</td>
         </tr>
         """.format(i.get_total())
    return mark_safe(items_li)


@register.simple_tag
def shipping_li():
    items = Shipping.objects.filter(isActive=True)
    shipping_li = ""
    for i in items:
        shipping_li += """
               <p>{} <span> {}</span></p>              
         """.format(
            i.location, i.charge)
    return mark_safe(shipping_li)
