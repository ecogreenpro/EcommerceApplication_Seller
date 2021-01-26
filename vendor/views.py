from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import render
from django.contrib import messages, auth
# Create your views here.
from django.views.generic import ListView, DetailView, View, UpdateView

from core.models import Products, OrderProduct, Order
from vendor.forms import SellerRegistrationForm, AddProductForm, OrderUpdateForm, sellerProfile


def vendorDashboard(request):
    context = {}
    return render(request, 'vendor/vendorDashboard.html', context)


# class allProduct(ListView):
#     model = Products
#     paginate_by = 16
#     template_name = "vendor/allProduct.html"



def allProduct(request):
    product = Products.objects.all()
    context = {
        'product':product
    }
    return render(request, 'vendor/allProduct.html', context)


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
        }
        return render(self.request, "vendor/vendorOrderDetails.html", context)


# class OrderUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
#     model = Order
#     fields = ['order_status']
#
#     def form_valid(self, form):
#         form.instance.author = self.request.user
#         return super().form_valid(form)


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


def settings(request):
    if request.method == 'POST':
        Name = request.POST['Name']
        ShopName = request.POST['ShopName']
        Address = request.POST['Address']
        Phone = request.POST['Phone']
        Email = request.POST['Email']

        sellerProfile.objects.filter(user=request.user).update(Name=Name, Address=Address,
                                                               ShopName=ShopName,
                                                               Phone=Phone, Email=Email)

    return render(request, 'vendor/settings.html')


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
