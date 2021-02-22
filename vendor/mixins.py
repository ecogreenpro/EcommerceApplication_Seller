from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Sum
from core.models import Products, OrderProduct


class SellerAccountMixin(LoginRequiredMixin, object):
    def get_total_sales(self):
        user = self.request.user
        products = Products.objects.filter(user=user)
        productPrice = OrderProduct.objects.filter(product__in=products)
        transactions = productPrice.aggregate(Sum("price"))
        total_sales = transactions["price__sum"]
        return total_sales
