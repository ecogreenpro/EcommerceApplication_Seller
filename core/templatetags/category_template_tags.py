from django import template
from django.utils.safestring import mark_safe

from core.models import Categories, Brands

register = template.Library()


@register.simple_tag
def categories():
    items = Categories.objects.filter(isactive=True).order_by('name')
    items_li = ""
    for i in items:
        items_li += """<li><a href="/category/{}"><i class="icon-shirt"></i> {}</a></li>""".format(
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
        items_li += """ <div class="col-xl-2 col-lg-3 col-md-4 col-sm-4 col-6 ">
                               <div class="ps-block&#45;&#45;category"><a class="ps-block__overlay" href="/category/{}"></a>
                               <img
                                   src="media/{}" alt="">
                               <p>{}</p>
                               </div>
                           </div>""".format(
            i.slug, i.image, i.name)
    return mark_safe(items_li)


@register.simple_tag
def brand_shop():
    items = Brands.objects.filter(isactive=True).order_by('name')
    items_li = ""
    for i in items:
        items_li += """<li><a href="/brand/{}">{} </a><span></span></li>""".format(
            i.slug, i.name)
    return mark_safe(items_li)
