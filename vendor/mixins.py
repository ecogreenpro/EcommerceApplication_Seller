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

    def get_seller_order(self):
        user = self.request.user
        products = Products.objects.filter(user=user)
        orders = OrderProduct.objects.filter(product__in=products)
        return orders

    def get_seller_order_count(self):
        user = self.request.user
        products = Products.objects.filter(user=user)
        orders = OrderProduct.objects.filter(product__in=products).count
        return orders

    def seller_product(self):
        product = Products.objects.filter(user=self.request.user)
        return product

    def seller_product_count(self):
        product = Products.objects.filter(user=self.request.user).count()
        return product

