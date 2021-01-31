from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib import messages, auth
# Create your views here.
from django.views.generic import ListView, DetailView, View, UpdateView

from core.models import Products, OrderProduct, Order, Settings
from vendor.forms import SellerRegistrationForm, AddProductForm, sellerProfile, ProfileUpdateForm, updateForm
from vendor.models import SellerRegistration


@login_required(login_url='/login')
def vendorDashboard(request):
    context = {}
    return render(request, 'vendor/vendorDashboard.html', context)


def becomeSeller(request):
    setting = Settings.objects.get()
    if request.method == 'POST':
        form = SellerRegistrationForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            messages.info(request, 'Registration Confirmed')
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
    product = Products.objects.filter(user=request.user)
    context = {
        'product': product
    }
    return render(request, 'vendor/allProduct.html', context)


@login_required(login_url='/login')
def addProduct(request):
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
    return render(request, 'vendor/addProduct.html', {'form': form})


@login_required(login_url='/login')
def vendoerStockmanager(request):
    context = {}
    return render(request, 'vendor/vendoerStockmanager.html', context)


@login_required(login_url='/login')
def vendoerOrderManager(request):
    orders = Order.objects.all()
    context = {
        'myOrders': orders
    }
    return render(request, 'vendor/vendoerOrderManager.html', context)


class vandorOrderDetails(DetailView):
    def get(self, *args, **kwargs):
        order = Order.objects.get(order_Number=self.kwargs['order_Number'])
        orderProdcut = OrderProduct.objects.filter(order=order)
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
            'OrderStatus': order.order_status
        }
        return render(self.request, "vendor/vendorOrderDetails.html", context)


@login_required(login_url='/login')
def vendorReviewManager(request):
    context = {}
    return render(request, 'vendor/vendorReview.html', context)


@login_required(login_url='/login')
def salesReport(request):
    context = {}
    return render(request, 'vendor/salesReport.html', context)


@login_required(login_url='/login')
def topSelling(request):
    context = {}
    return render(request, 'vendor/topSelling.html', context)


@login_required(login_url='/login')
def accountsReport(request):
    context = {}
    return render(request, 'vendor/accountsReport.html', context)


@login_required(login_url='/login')
def settings(request):
    return render(request, 'vendor/sellerProfile.html')


@login_required(login_url='/login')
def updateProduct(request, slug):
    product = Products.objects.filter(slug=slug).first()
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

            'form': productUpdateForm
        }
        return render(request, 'vendor/updateProduct.html', context)


@login_required(login_url='/login')  # Check login
def sellerUpdate(request):
    shopDetails = SellerRegistration.objects.filter(ShopName=request.user.sellerprofile.ShopDetails.ShopName).first()
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

            'shopDetailsForm': shopDetailsForm
        }
        return render(request, 'vendor/sellerDetailsUpdate.html', context)


@login_required(login_url='/login')
def sellerChangePassword(request):
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
