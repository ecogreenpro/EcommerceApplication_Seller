from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.forms import PasswordChangeForm
from django.db.models import Sum
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib import messages
from django.views.generic import DetailView, View
from core.models import Products, OrderProduct, Order, Settings
from vendor.forms import SellerRegistrationForm, AddProductForm, sellerProfile, ProfileUpdateForm, updateForm
from vendor.mixins import SellerAccountMixin
from vendor.models import SellerRegistration


def becomeSeller(request):
    setting = Settings.objects.get()
    if request.method == 'POST':
        form = SellerRegistrationForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            messages.info(request, 'Seller Registration Confirmed, We Will mail you shortly')
            return HttpResponseRedirect('/login/')
    else:
        form = SellerRegistrationForm()
    return render(request, 'becomeSeller.html', {'form': form, 'Settings': setting})


class SellerDashboard(SellerAccountMixin, View):
    def get(self, request, *args, **kwargs):
        seller = sellerProfile.objects.filter(user=self.request.user)
        total_sales = self.get_total_sales()
        orders = self.get_seller_order()
        orderCount = self.get_seller_order_count()
        products = self.seller_product()
        productCount = self.seller_product_count()
        setting = Settings.objects.get()
        context = {
            'total_sales': total_sales,
            'Settings': setting,
            'sellerOrder': orders,
            'orderCount': orderCount,
            'sellerProduct': products,
            'productCount': productCount

        }
        if seller.exists():
            return render(request, 'vendor/vendorDashboard.html', context)
        else:
            form = SellerRegistrationForm()
            messages.warning(request, 'You are not a Jewellery Seller')
            return render(request, 'becomeSeller.html', {'form': form})


class allProduct(SellerAccountMixin, View):
    def get(self, request):
        user = request.user
        seller = sellerProfile.objects.filter(user=user)
        setting = Settings.objects.get()
        total_sales = self.get_total_sales()

        if seller.exists():

            product = Products.objects.filter(user=request.user)
            context = {
                'product': product,
                'Settings': setting,
                'total_sales': total_sales
            }
            return render(request, 'vendor/allProduct.html', context)
        else:
            form = SellerRegistrationForm()
            context = {
                'Settings': setting,
                'form': form,
            }
            messages.warning(request, 'You are not a Jewellery Seller')
            return render(request, 'becomeSeller.html', context)


class addProduct(SellerAccountMixin, View):
    def get(self, request):
        user = request.user
        seller = sellerProfile.objects.filter(user=user)
        total_sales = self.get_total_sales()
        setting = Settings.objects.get()
        if seller.exists():
            if request.method == 'POST':
                form = AddProductForm(request.POST, request.FILES, request=request)

                if form.is_valid():
                    form.save()
                    messages.info(request, 'Product Added Successfully, We will review your Product.')
                    return HttpResponseRedirect('/all-product/')
                else:
                    messages.error(request, 'Please correct the error below.<br>' + str(form.errors))
                    return HttpResponseRedirect('/add-new-product/')
            else:
                form = AddProductForm(request=request)
                context = {
                    'Settings': setting,
                    'form': form,
                    'total_sales': total_sales
                }

            return render(request, 'vendor/addProduct.html', context)
        else:
            form = SellerRegistrationForm()
            context = {
                'Settings': setting,
                'form': form,
            }
            messages.warning(request, 'You are not a Jewellery Seller')
            return render(request, 'becomeSeller.html', context)


@login_required(login_url='/login')
def vendoerStockmanager(request):
    context = {}
    return render(request, 'vendor/vendoerStockmanager.html', context)


class vendoerOrderManager(SellerAccountMixin, View):
    def get(self, request):
        user = request.user
        products = Products.objects.filter(user=request.user)
        orders = OrderProduct.objects.filter(product__in=products)
        total_sales = self.get_total_sales()
        seller = sellerProfile.objects.filter(user=user)
        setting = Settings.objects.get()
        if seller.exists():
            context = {
                'myOrders': orders,
                'Settings': setting,
                'total_sales': total_sales
            }
            return render(request, 'vendor/vendoerOrderManager.html', context)
        else:
            form = SellerRegistrationForm()
            context = {
                'Settings': setting,
                'form': form,

            }
            messages.warning(request, 'You are not a Jewellery Seller')
            return render(request, 'becomeSeller.html', context)


class vandorOrderDetails(SellerAccountMixin, View):
    def get(self, request, *args, **kwargs):
        order = Order.objects.get(order_Number=self.kwargs['order_Number'])
        orderProdcut = OrderProduct.objects.filter(order=order)
        total_sales = self.get_total_sales()
        user = request.user
        seller = sellerProfile.objects.filter(user=user)
        setting = Settings.objects.get()
        if seller.exists():
            context = {
                'Product': orderProdcut,
                'Billed_firstName': order.first_name,
                'Billed_lastName': order.last_name,
                'Phone': order.phone_number,
                'Email': order.email,
                'Address': order.address,
                'District': order.district,
                'Country': order.country,
                'OrderDate': order.ordered_date,
                'OrderNo': order.order_Number,
                'oderTotal': order.OrderTotal,
                'Delivery': order.payment,
                'OrderNote': order.order_note,
                'OrderStatus': order.order_status,
                'Settings': setting,
                'total_sales': total_sales,
            }
            return render(self.request, "vendor/vendorOrderDetails.html", context)
        else:
            form = SellerRegistrationForm()
            context = {
                'Settings': setting,
                'form': form,

            }
            messages.warning(request, 'You are not a Jewellery Seller')
            return render(request, 'becomeSeller.html', context)


@login_required(login_url='/login')
def vendorReviewManager(request):
    setting = Settings.objects.get()
    context = {'Settings': setting, }
    return render(request, 'vendor/vendorReview.html', context)


@login_required(login_url='/login')
def salesReport(request):
    setting = Settings.objects.get()
    context = {'Settings': setting, }
    return render(request, 'vendor/salesReport.html', context)


@login_required(login_url='/login')
def topSelling(request):
    setting = Settings.objects.get()
    context = {'Settings': setting, }
    return render(request, 'vendor/topSelling.html', context)


@login_required(login_url='/login')
def accountsReport(request):
    setting = Settings.objects.get()
    context = {'Settings': setting, }
    return render(request, 'vendor/accountsReport.html', context)


class settings(SellerAccountMixin, View):
    def get(self, request):
        user = request.user
        seller = sellerProfile.objects.filter(user=user)
        total_sales = self.get_total_sales()
        setting = Settings.objects.get()
        if seller.exists():
            context = {'Settings': setting,
                       'total_sales': total_sales
                       }
            return render(request, 'vendor/sellerProfile.html', context)
        else:
            form = SellerRegistrationForm()
            context = {
                'Settings': setting,
                'form': form,
            }
            messages.warning(request, 'You are not a Jewellery Seller')
            return render(request, 'becomeSeller.html', context)


class updateProduct(SellerAccountMixin, View):
    def get(self, request, slug):
        product = Products.objects.filter(slug=slug).first()
        user = request.user
        seller = sellerProfile.objects.filter(user=user)
        total_sales = self.get_total_sales()
        setting = Settings.objects.get()
        if seller.exists():
            if request.method == 'POST':
                productUpdateForm = updateForm(request.POST, request.FILES,
                                               instance=product)
                if productUpdateForm.is_valid():
                    productUpdateForm.save()
                    messages.success(request, 'Your Product has been updated!')
                    return HttpResponseRedirect('/all-product/')
            else:

                productUpdateForm = updateForm(instance=product)
                context = {

                    'form': productUpdateForm,
                    'Settings': setting,
                    'total_sales': total_sales
                }
                return render(request, 'vendor/updateProduct.html', context)
        else:
            form = SellerRegistrationForm()
            context = {
                'Settings': setting,
                'form': form,
            }
            messages.warning(request, 'You are not a Jewellery Seller')
            return render(request, 'becomeSeller.html', context)


class sellerUpdate(SellerAccountMixin, View):
    def get(self, request):
        shopDetails = SellerRegistration.objects.filter(
            ShopName=request.user.sellerprofile.ShopDetails.ShopName).first()
        user = request.user
        total_sales = self.get_total_sales()
        seller = sellerProfile.objects.filter(user=user)
        setting = Settings.objects.get()
        if seller.exists():
            if request.method == 'POST':
                shopDetailsForm = ProfileUpdateForm(request.POST, request.FILES,
                                                    instance=shopDetails)
                if shopDetailsForm.is_valid():
                    shopDetailsForm.save()
                    messages.success(request, 'Your account has been updated!')
                    return HttpResponseRedirect('/seller-profile/')
            else:

                shopDetailsForm = ProfileUpdateForm(instance=shopDetails)
                context = {

                    'shopDetailsForm': shopDetailsForm,
                    'Settings': setting,
                    'total_sales': total_sales
                }
                return render(request, 'vendor/sellerDetailsUpdate.html', context)
        else:
            form = SellerRegistrationForm()
            context = {
                'Settings': setting,
                'form': form,
            }
            messages.warning(request, 'You are not a Jewellery Seller')
            return render(request, 'becomeSeller.html', context)


class sellerChangePassword(SellerAccountMixin, View):
    def get(self, request):
        user = request.user
        seller = sellerProfile.objects.filter(user=user)
        total_sales = self.get_total_sales()
        setting = Settings.objects.get()
        if seller.exists():
            if request.method == 'POST':
                form = PasswordChangeForm(request.user, request.POST)
                if form.is_valid():
                    user = form.save()
                    update_session_auth_hash(request, user)  # Important!
                    messages.success(request, 'Your password was successfully updated!')
                    return HttpResponseRedirect('/seller-profile')
                else:
                    messages.error(request, 'Please correct the error below.<br>' + str(form.errors))
                    return HttpResponseRedirect('/seller-change-password/')
            else:

                form = PasswordChangeForm(request.user)
                return render(request, 'vendor/sellerChangePassword.html', {'form': form, 'total_sales': total_sales})
        else:
            form = SellerRegistrationForm()
            context = {
                'Settings': setting,
                'form': form,
            }
            messages.warning(request, 'You are not a Jewellery Seller')
            return render(request, 'becomeSeller.html', context)


# Super admin part

class allseller(SellerAccountMixin, View):
    def get(self, request):
        total_sales = self.get_total_sales()
        seller = sellerProfile.objects.all()
        setting = Settings.objects.get()
        if seller.exists():
            context = {
                'Settings': setting,
                'sellers': seller,
                'total_sales': total_sales

            }
            return render(request, 'superUser/allSeller.html', context)
        else:
            form = SellerRegistrationForm()
            context = {
                'Settings': setting,
                'form': form,
            }
            messages.warning(request, 'You are not a Jewellery Seller')
            return render(request, 'becomeSeller.html', context)


class sellerDetails(SellerAccountMixin, View):
    def get(self, request, *args, **kwargs):
        total_sales = self.get_total_sales()
        sellerUser = sellerProfile.objects.filter(Seller_id=self.kwargs['Seller_id']).first()
        setting = Settings.objects.get()
        context = {

            'Settings': setting,
            'seller': sellerUser,
            'total_sales': total_sales
        }
        return render(self.request, "superUser/superUserSellerDetails.html", context)


class sellerInfoReport(View):
    def get(self, request, *args, **kwargs):
        sellerUser = sellerProfile.objects.filter(Seller_id=self.kwargs['Seller_id']).first()
        setting = Settings.objects.get()
        context = {

            'Settings': setting,
            'seller': sellerUser,
        }
        return render(self.request, "superUser/sellerInfoReport.html", context)


class sellerRequest(SellerAccountMixin, View):
    def get(self, request):
        sellerreq = SellerRegistration.objects.all()
        total_sales = self.get_total_sales()
        setting = Settings.objects.get()
        if sellerreq.exists():
            context = {
                'Settings': setting,
                'sellers': sellerreq,
                'total_sales': total_sales

            }
            return render(request, 'superUser/sellerRequest.html', context)
        else:
            form = SellerRegistrationForm()
            context = {
                'Settings': setting,
                'form': form,
            }
            messages.warning(request, 'You are not a Jewellery Seller')
            return render(request, 'becomeSeller.html', context)


class sellerRequestDetails(SellerAccountMixin, View):
    def get(self, request, pk, *args, **kwargs):
        total_sales = self.get_total_sales()
        sellers = SellerRegistration.objects.filter(id=self.kwargs['pk']).first()
        setting = Settings.objects.get()
        context = {

            'Settings': setting,
            'seller': sellers,
            'total_sales': total_sales
        }
        return render(self.request, "superUser/sellerRequestDetails.html", context)
