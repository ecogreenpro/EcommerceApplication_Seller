from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib import messages, auth
# Create your views here.
from django.views.generic import ListView, DetailView, View, UpdateView

from core.models import Products, OrderProduct, Order, Settings, userProfile
from vendor.forms import SellerRegistrationForm, AddProductForm, sellerProfile, ProfileUpdateForm, updateForm
from vendor.models import SellerRegistration


@login_required(login_url='/login')
def vendorDashboard(request):
    user = request.user
    seller = sellerProfile.objects.filter(user=user)
    setting = Settings.objects.get()
    if seller.exists():
        return render(request, 'vendor/vendorDashboard.html', {'Settings': setting})
    else:
        form = SellerRegistrationForm()
        messages.warning(request, 'You are not a Jewellery Seller')
        return render(request, 'becomeSeller.html', {'form': form})


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


# class allProduct(ListView):
#     model = Products
#     paginate_by = 16
#     template_name = "vendor/allProduct.html"

@login_required(login_url='/login')
def allProduct(request):
    user = request.user
    seller = sellerProfile.objects.filter(user=user)
    setting = Settings.objects.get()
    if seller.exists():

        product = Products.objects.filter(user=request.user)
        context = {
            'product': product,
            'Settings': setting,
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


@login_required(login_url='/login')
def addProduct(request):
    user = request.user
    seller = sellerProfile.objects.filter(user=user)
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
                'form': form
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


@login_required(login_url='/login')
def vendoerOrderManager(request):
    user = request.user
    products = Products.objects.filter(user=request.user)
    orders = OrderProduct.objects.filter(product__in=products)
    seller = sellerProfile.objects.filter(user=user)
    setting = Settings.objects.get()
    if seller.exists():
        context = {
            'myOrders': orders,
            'Settings': setting,
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


class vandorOrderDetails(DetailView):
    def get(self, request, *args, **kwargs):
        order = Order.objects.get(order_Number=self.kwargs['order_Number'])
        orderProdcut = OrderProduct.objects.filter(order=order)
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


@login_required(login_url='/login')
def settings(request):
    user = request.user
    seller = sellerProfile.objects.filter(user=user)
    setting = Settings.objects.get()
    if seller.exists():
        context = {'Settings': setting, }
        return render(request, 'vendor/sellerProfile.html', context)
    else:
        form = SellerRegistrationForm()
        context = {
            'Settings': setting,
            'form': form,
        }
        messages.warning(request, 'You are not a Jewellery Seller')
        return render(request, 'becomeSeller.html', context)


@login_required(login_url='/login')
def updateProduct(request, slug):
    product = Products.objects.filter(slug=slug).first()
    user = request.user
    seller = sellerProfile.objects.filter(user=user)
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


@login_required(login_url='/login')  # Check login
def sellerUpdate(request):
    shopDetails = SellerRegistration.objects.filter(ShopName=request.user.sellerprofile.ShopDetails.ShopName).first()
    user = request.user
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


@login_required(login_url='/login')
def sellerChangePassword(request):
    user = request.user
    seller = sellerProfile.objects.filter(user=user)
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
            return render(request, 'vendor/sellerChangePassword.html', {'form': form, })
    else:
        form = SellerRegistrationForm()
        context = {
            'Settings': setting,
            'form': form,
        }
        messages.warning(request, 'You are not a Jewellery Seller')
        return render(request, 'becomeSeller.html', context)


@user_passes_test(lambda u: u.is_superuser)
@login_required(login_url='/login/')
def allSeller(request):
    seller = sellerProfile.objects.all()
    setting = Settings.objects.get()
    if seller.exists():
        context = {
            'Settings': setting,
            'sellers': seller

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


class sellerDetails(View):
    def get(self, request, *args, **kwargs):
        sellerUser = sellerProfile.objects.filter(Seller_id=self.kwargs['Seller_id']).first()
        setting = Settings.objects.get()
        context = {

            'Settings': setting,
            'seller': sellerUser,
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


@user_passes_test(lambda u: u.is_superuser)
@login_required(login_url='/login/')
def sellerRequest(request):
    sellerreq = SellerRegistration.objects.all()
    setting = Settings.objects.get()
    if sellerreq.exists():
        context = {
            'Settings': setting,
            'sellers': sellerreq

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
