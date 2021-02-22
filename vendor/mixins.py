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

# class SellerDashboard(SellerAccountMixin, View):
#     @login_required(login_url='/login')
#     def get(self, request, *args, **kwargs):
#         seller = sellerProfile.objects.filter(user=self.request.user)
#         total_sales = self.get_total_sales()
#         setting = Settings.objects.get()
#         context = {
#             'total_sales': total_sales,
#             'Settings': setting
#         }
#
#         if seller.exists():
#             return render(self.request, 'vendor/vendorDashboard.html', context)
#         else:
#             form = SellerRegistrationForm()
#             messages.warning(self.request, 'You are not a Jewellery Seller')
#             return render(self.request, 'becomeSeller.html', {'form': form})