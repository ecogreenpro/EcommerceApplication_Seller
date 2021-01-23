from django.shortcuts import render
from django.contrib import messages, auth
# Create your views here.
from django.views.generic import ListView

from core.models import Products, OrderProduct
from vendor.forms import SellerRegistrationForm, AddProductForm


def vendorDashboard(request):
    context = {}
    return render(request, 'vendor/vendorDashboard.html', context)


class allProduct(ListView):
    model = Products
    paginate_by = 16
    template_name = "vendor/allProduct.html"


#
# def allProduct(request):
#     context = {}
#     return render(request, 'vendor/allProduct.html', context)


def addProduct(request):
    if request.method == 'POST':
        form = AddProductForm(request.POST, request.FILES, request=request)

        if form.is_valid():
            form.save()
            messages.info(request, 'Product Added Successfully, We will review your Product.')
            return render(request, 'vendor/allProduct.html')
    else:
        form = AddProductForm(request=request)
    return render(request, 'vendor/addProduct.html', {'form': form})


def vendoerStockmanager(request):
    context = {}
    return render(request, 'vendor/vendoerStockmanager.html', context)


def vendoerOrderManager(request):
    orders = OrderProduct.objects.all()
    context = {
        'myOrders': orders
    }
    return render(request, 'vendor/vendoerOrderManager.html', context)


def vendorReviewManager(request):
    context = {}
    return render(request, 'vendor/vendorReview.html', context)


def salesReport(request):
    context = {}
    return render(request, 'vendor/salesReport.html', context)


def topSelling(request):
    context = {}
    return render(request, 'vendor/topSelling.html', context)


def accountsReport(request):
    context = {}
    return render(request, 'vendor/accountsReport.html', context)


def becomeSeller(request):
    if request.method == 'POST':
        form = SellerRegistrationForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            messages.info(request, 'Registration Confirmed')
            return render(request, 'account/login.html')
    else:
        form = SellerRegistrationForm()
    return render(request, 'becomeSeller.html', {'form': form})
