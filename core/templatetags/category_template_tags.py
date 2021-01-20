from django import template
from django.utils.safestring import mark_safe

from core.models import Categories, Brands

register = template.Library()


@register.simple_tag
def categories():
    items = Categories.objects.filter(isactive=True).order_by('name')
    items_li = ""
    for i in items:
        items_li += """<a href="/category/{}" class="list-group-item list-group-item-action text-white" style="background-color: #ac801cc2!important; font-family: 'Rubik';"><i 
        class="fas fa-th-large"></i> {}</a>""".format(
            i.slug, i.name)
    return mark_safe(items_li)


@register.simple_tag
def categories_shop():
    items = Categories.objects.filter(isactive=True).order_by('name')
    items_li = ""


    for i in items:
        items_li += """<li class="nav-item"><a class="nav-link" href="/category/{}"></i>{}</a></li>""".format(
            i.slug, i.name, i.image)
    return mark_safe(items_li)


@register.simple_tag
def categories_home():
    items = Categories.objects.filter(isactive=True).order_by('name')
    items_li = ""
    for i in items:
        items_li += """ <div class="col-lg-3">
                                    <div class="product-item">
                                        <div class="product-title">
                                            <a style="text-decoration: none;" href="/category/{}">{}</a>
                                            
                                        </div>
                                        <div class="product-image">
                                            <a style="text-decoration: none;"  href="/category/{}">
                                                <img class="image" src="media/{}" alt="Product Image">
                                            </a>
                                        </div>
                                        <div class="product-price">
                                            <h3><span> </span><label >Jewellery</label> </h3>
                                            <a style="text-decoration: none;" href="/category/{}" class="btn" href=""><i class="far fa-eye"></i> Shop Now</a>
                                        </div>
                                    </div>
                                </div>""".format(
            i.slug,i.name, i.slug, i.image,i.slug)
    return mark_safe(items_li)


@register.simple_tag
def brand_shop():
    items = Brands.objects.filter(isactive=True).order_by('name')
    items_li = ""
    for i in items:
        items_li += """<li><a href="/brand/{}">{} </a><span></span></li>""".format(
            i.slug, i.name)
    return mark_safe(items_li)
