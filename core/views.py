from django.contrib import messages, auth
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.http import HttpResponseRedirect
from django.template.loader import get_template
from django.utils import timezone
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404, redirect
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, View
from django.utils.crypto import get_random_string

from .forms import ProfileUpdateForm
from .models import Products, CartProducts, Order, userProfile, OrderProduct, Shipping, Settings, CarouselAdvImage
from .models import Products, Categories, Brands
from vendor.models import sellerProfile


# Create your views here.


def header(request):
    images = CarouselAdvImage.objects.get()
    setting = Settings.objects.get()
    if request.user.is_authenticated:
        cart = CartProducts.objects.filter(user=request.user)
        total = 0
        for rs in cart:
            if rs.item.discountPrice:
                total += rs.item.discountPrice * rs.quantity
            else:
                total += rs.item.price * rs.quantity
        context = {
            'Settings': setting,
            'cart': cart,
            'image': images,
            'total': total,
        }
        return render(request, 'header.html', context)
    else:
        context = {
            'Settings': setting,
            'images': images,
        }
        return render(request, 'header.html', context)


def footer(request):
    setting = Settings.objects.get()
    context = {'Settings': setting}
    return render(request, 'footer.html', context)


def about(request):
    setting = Settings.objects.get()
    images = CarouselAdvImage.objects.get()
    if request.user.is_authenticated:
        cart = CartProducts.objects.filter(user=request.user)
        total = 0
        for rs in cart:
            if rs.item.discountPrice:
                total += rs.item.discountPrice * rs.quantity
            else:
                total += rs.item.price * rs.quantity
        context = {
            'Settings': setting,
            'cart': cart,
            'image': images,
            'total': total,
        }
        return render(request, 'base/about.html', context)
    else:
        context = {
            'Settings': setting,
            'images': images,

        }
        return render(request, 'base/about.html', context)


def contact(request):
    setting = Settings.objects.get()
    images = CarouselAdvImage.objects.get()
    if request.user.is_authenticated:
        cart = CartProducts.objects.filter(user=request.user)
        total = 0
        for rs in cart:
            if rs.item.discountPrice:
                total += rs.item.discountPrice * rs.quantity
            else:
                total += rs.item.price * rs.quantity
        context = {
            'Settings': setting,
            'cart': cart,
            'image': images,
            'total': total
        }
        return render(request, 'base/contact.html', context)
    else:
        context = {
            'Settings': setting,
            'image': images,
        }
        return render(request, 'base/contact.html', context)


def privacyPolicy(request):
    setting = Settings.objects.get()
    if request.user.is_authenticated:
        cart = CartProducts.objects.filter(user=request.user)
        total = 0
        for rs in cart:
            if rs.item.discountPrice:
                total += rs.item.discountPrice * rs.quantity
            else:
                total += rs.item.price * rs.quantity
        context = {
            'Settings': setting,
            'cart': cart,
            'total': total
        }
        return render(request, 'base/privacyPolicy.html', context)
    else:
        context = {
            'Settings': setting,
        }
        return render(request, 'base/privacyPolicy.html', context)


def terms(request):
    setting = Settings.objects.get()
    if request.user.is_authenticated:
        cart = CartProducts.objects.filter(user=request.user)
        total = 0
        for rs in cart:
            if rs.item.discountPrice:
                total += rs.item.discountPrice * rs.quantity
            else:
                total += rs.item.price * rs.quantity
        context = {
            'Settings': setting,
            'cart': cart,
            'total': total
        }
        return render(request, 'base/refundReturnsPolicy.html', context)
    else:
        context = {
            'Settings': setting,
        }
        return render(request, 'base/refundReturnsPolicy.html', context)


def paymentProcess(request):
    setting = Settings.objects.get()
    if request.user.is_authenticated:
        cart = CartProducts.objects.filter(user=request.user)
        total = 0
        for rs in cart:
            if rs.item.discountPrice:
                total += rs.item.discountPrice * rs.quantity
            else:
                total += rs.item.price * rs.quantity
        context = {
            'Settings': setting,
            'cart': cart,
            'total': total
        }
        return render(request, 'base/paymentProcess.html', context)
    else:
        context = {
            'Settings': setting,
        }
        return render(request, 'base/paymentProcess.html', context)


def login(request):
    setting = Settings.objects.get()
    if request.user.is_authenticated:
        cart = CartProducts.objects.filter(user=request.user)
        total = 0
        for rs in cart:
            if rs.item.discountPrice:
                total += rs.item.discountPrice * rs.quantity
            else:
                total += rs.item.price * rs.quantity
        context = {
            'Settings': setting,
            'cart': cart,
            'total': total
        }
        if request.method == "POST":
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = auth.authenticate(username=username, password=password)
            if user is not None:
                auth.login(request, user)
                return render(request, 'account/userprofile.html')
            else:
                messages.info(request, 'Invalid Login')
        else:
            return render(request, 'account/login.html', context)
        return HttpResponseRedirect(request, '/user-profile/', context)
    else:
        context = {
            'Settings': setting,
        }
        if request.method == "POST":
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = auth.authenticate(username=username, password=password)
            if user is not None:
                auth.login(request, user)
                return render(request, 'account/userprofile.html')
            else:
                messages.info(request, 'Invalid Login')
        else:
            return render(request, 'account/login.html', context)
        return render(request, 'account/login.html', context)


def logout(request):
    auth.logout(request)
    messages.info(request, 'Successfully Logout')
    return redirect('/login/')


def dashboard(request):
    context = {}
    return render(request, 'account/dashboard.html', context)


def forgotpassword(request):
    setting = Settings.objects.get()
    if request.user.is_authenticated:
        cart = CartProducts.objects.filter(user=request.user)
        total = 0
        for rs in cart:
            if rs.item.discountPrice:
                total += rs.item.discountPrice * rs.quantity
            else:
                total += rs.item.price * rs.quantity
        context = {
            'Settings': setting,
            'cart': cart,
            'total': total
        }
        return render(request, 'account/forgotpassword.html', context)
    else:
        context = {
            'Settings': setting,
        }
        return render(request, 'account/forgotpassword.html', context)


@login_required(login_url='/login')
def changePassword(request):
    setting = Settings.objects.get()
    if request.user.is_authenticated:
        cart = CartProducts.objects.filter(user=request.user)
        total = 0
        for rs in cart:
            if rs.item.discountPrice:
                total += rs.item.discountPrice * rs.quantity
            else:
                total += rs.item.price * rs.quantity
        context = {
            'Settings': setting,
            'cart': cart,
            'total': total
        }
        if request.method == 'POST':
            form = PasswordChangeForm(request.user, request.POST)
            if form.is_valid():
                user = form.save()
                update_session_auth_hash(request, user)  # Important!
                messages.success(request, 'Your password was successfully updated!')
                return HttpResponseRedirect('/user-profile/')
            else:
                messages.error(request, 'Please correct the error below.<br>' + str(form.errors))
                return HttpResponseRedirect('/change-password/')
        else:

            form = PasswordChangeForm(request.user)
            return render(request, 'account/ChangePassword.html', {'form': form,  'Settings': setting})
    else:
        context = {
            'Settings': setting,
        }
        if request.method == 'POST':
            form = PasswordChangeForm(request.user, request.POST)
            if form.is_valid():
                user = form.save()
                update_session_auth_hash(request, user)  # Important!
                messages.success(request, 'Your password was successfully updated!')
                return HttpResponseRedirect('/userprofile')
            else:
                messages.error(request, 'Please correct the error below.<br>' + str(form.errors))
                return HttpResponseRedirect('/change-password/')
        else:

            form = PasswordChangeForm(request.user)
            return render(request, 'account/ChangePassword.html', {'form': form, }, context)


def signup(request):
    setting = Settings.objects.get()
    if request.user.is_authenticated:
        cart = CartProducts.objects.filter(user=request.user)
        total = 0
        for rs in cart:
            if rs.item.discountPrice:
                total += rs.item.discountPrice * rs.quantity
            else:
                total += rs.item.price * rs.quantity
        context = {
            'Settings': setting,
            'cart': cart,
            'total': total
        }
        return render(request, 'account/signup.html', context)
    else:
        context = {
            'Settings': setting,
        }
        return render(request, 'account/signup.html', context)


def createUser(request):
    setting = Settings.objects.get()
    if request.user.is_authenticated:
        cart = CartProducts.objects.filter(user=request.user)
        total = 0
        for rs in cart:
            if rs.item.discountPrice:
                total += rs.item.discountPrice * rs.quantity
            else:
                total += rs.item.price * rs.quantity
        context = {
            'Settings': setting,
            'cart': cart,
            'total': total
        }
        first_name = request.POST['firstName']
        last_name = request.POST['lastName']
        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['password']
        if User.objects.filter(email=email).exists():
            messages.warning(request, 'This Email already taken')
            return redirect('account/signup.html')
        else:
            if User.objects.filter(username=username).exists():
                messages.warning(request, 'This username already taken,Please Choose another one')
                return redirect('account/signup.html')
            else:
                userRegistration = User.objects.create_user(username=username, first_name=first_name,
                                                            last_name=last_name,
                                                            email=email,
                                                            password=password)
                userRegistration.is_staff = False
                userRegistration.save()
                messages.info(request, 'Registration Confirmed')
        return render(request, 'account/login.html', context)
    else:
        context = {
            'Settings': setting,
        }
        first_name = request.POST['firstName']
        last_name = request.POST['lastName']
        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['password']
        if User.objects.filter(email=email).exists():
            messages.warning(request, 'This Email already taken')
            return redirect('account/signup.html')
        else:
            if User.objects.filter(username=username).exists():
                messages.warning(request, 'This username already taken,Please Choose another one')
                return redirect('account/signup.html')
            else:
                userRegistration = User.objects.create_user(username=username, first_name=first_name,
                                                            last_name=last_name,
                                                            email=email,
                                                            password=password)
                userRegistration.is_staff = False
                userRegistration.save()
                messages.info(request, 'Registration Confirmed')
        return render(request, 'account/login.html', context)


@login_required(login_url='/login')  # Check login
def updateProfile(request):
    setting = Settings.objects.get()
    if request.method == 'POST':
        profile_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.userprofile)
        if profile_form.is_valid():
            profile_form.save()
            messages.success(request, 'Your account has been updated!')
            return HttpResponseRedirect('/user-profile/')
    else:
        profile_form = ProfileUpdateForm(instance=request.user.userprofile)
        context = {
            'form': profile_form,
            'Settings': setting,
        }
        return render(request, 'account/updateProfile.html', context)


@login_required(login_url='/login')
def userprofile(request):
    setting = Settings.objects.get()
    profile_form = ProfileUpdateForm(instance=request.user.userprofile)
    if request.user.is_authenticated:
        cart = CartProducts.objects.filter(user=request.user)
        total = 0
        for rs in cart:
            if rs.item.discountPrice:
                total += rs.item.discountPrice * rs.quantity
            else:
                total += rs.item.price * rs.quantity
        context = {
            'Settings': setting,
            'cart': cart,
            'total': total, 'form': profile_form,

        }
        return render(request, 'account/userprofile.html', context)
    else:

        context = {
            'Settings': setting,
            'form': profile_form,
        }
        return render(request, 'account/userprofile.html', context)


@login_required(login_url='/login')
def userOrder(request):
    orders = Order.objects.filter(user=request.user)
    setting = Settings.objects.get()
    if request.user.is_authenticated:
        cart = CartProducts.objects.filter(user=request.user)
        total = 0
        for rs in cart:
            if rs.item.discountPrice:
                total += rs.item.discountPrice * rs.quantity
            else:
                total += rs.item.price * rs.quantity
        context = {
            'userorder': orders,
            'Settings': setting,
            'cart': cart,
            'total': total
        }
        return render(request, 'account/userOrder.html', context)
    else:

        context = {
            'userorder': orders,
            'Settings': setting,
        }
        return render(request, 'account/userOrder.html', context)


@login_required(login_url='/login')
def balance(request):
    setting = Settings.objects.get()
    if request.user.is_authenticated:
        cart = CartProducts.objects.filter(user=request.user)
        total = 0
        for rs in cart:
            if rs.item.discountPrice:
                total += rs.item.discountPrice * rs.quantity
            else:
                total += rs.item.price * rs.quantity
        context = {
            'Settings': setting,
            'cart': cart,
            'total': total
        }
        return render(request, 'account/balance.html', context)
    else:

        context = {
            'Settings': setting,

        }
        return render(request, 'account/balance.html', context)


class invoiceView(View):
    def get(self, *args, **kwargs):
        order = Order.objects.get(order_Number=self.kwargs['order_Number'])
        orderProdcut = OrderProduct.objects.filter(order=order)
        setting = Settings.objects.get()
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
            'Settings': setting,
        }
        return render(self.request, "account/invoice.html", context)


@login_required(login_url='/login')
def chat(request):
    setting = Settings.objects.get()
    if request.user.is_authenticated:
        cart = CartProducts.objects.filter(user=request.user)
        total = 0
        for rs in cart:
            if rs.item.discountPrice:
                total += rs.item.discountPrice * rs.quantity
            else:
                total += rs.item.price * rs.quantity
        context = {
            'Settings': setting,
            'cart': cart,
            'total': total
        }
        return render(request, 'account/chat.html', context)
    else:
        context = {
            'Settings': setting,
        }
        return render(request, 'account/chat.html', context)


@login_required(login_url='/login')
def cart(request):
    category = Categories.objects.all()  # Access User Session information
    cart = CartProducts.objects.filter(user=request.user)
    setting = Settings.objects.get()
    if cart:
        total = 0
        for rs in cart:
            if rs.item.discountPrice:
                total += rs.item.discountPrice * rs.quantity
            else:
                total += rs.item.price * rs.quantity
        context = {
            'cart': cart,
            'category': category,
            'total': total,
            'Settings': setting,
        }
    else:
        context = {"empty": True, 'Settings': setting}

    return render(request, 'cart.html', context)


@login_required(login_url='/login')
def checkout(request):
    current_user = request.user
    # shipping = Shipping.objects.all()
    category = Categories.objects.all()  # Access User Session information
    userprofile = userProfile.objects.get(user=request.user)
    cart = CartProducts.objects.filter(user=request.user)
    setting = Settings.objects.get()
    total = 100

    for rs in cart:
        if rs.item.discountPrice:
            total += rs.item.discountPrice * rs.quantity
        else:
            total += rs.item.price * rs.quantity
    if request.method == 'POST':
        data = Order()
        data.first_name = request.POST['firstName']  # get product quantity from form
        data.last_name = request.POST['lastName']
        data.phone_number = request.POST['mobile']
        data.email = request.POST['email']
        data.address = request.POST['address']
        data.district = request.POST['city']
        data.country = request.POST['country']
        data.zip_code = request.POST['zip']
        data.order_note = request.POST['note']
        data.payment = request.POST['paymentMethod']
        data.order_status = request.POST['orderStatus']
        data.user = current_user
        data.OrderTotal = total
        orderNumber = get_random_string(5).upper()  # random cod
        data.order_Number = orderNumber
        data.save()

        for rs in cart:
            productDetails = OrderProduct()
            product = Products.objects.get(id=rs.item_id)
            productDetails.order_id = data.id
            productDetails.product_id = rs.item_id
            productDetails.user_id = current_user.id
            productDetails.quantity = rs.quantity
            if rs.item.discountPrice:
                productDetails.price = rs.item.discountPrice
            else:
                productDetails.price = rs.item.price
            productDetails.amount = rs.get_final_price
            product.stockQuantity -= rs.quantity
            product.save()
            productDetails.save()

        CartProducts.objects.filter(user=request.user).delete()  # Clear & Delete shopcart
        request.session['cart_items'] = 0
        return render(request, 'orderComplete.html', {'orderCode': orderNumber})

    context = {
        'cart': cart,
        'category': category,
        'total': total,
        'userProfile': userprofile,
        'Settings': setting,
    }
    return render(request, 'checkout.html', context)


def orderTrack(request):
    setting = Settings.objects.get()
    if request.user.is_authenticated:
        cart = CartProducts.objects.filter(user=request.user)
        total = 0
        for rs in cart:
            if rs.item.discountPrice:
                total += rs.item.discountPrice * rs.quantity
            else:
                total += rs.item.price * rs.quantity
        context = {
            'Settings': setting,
            'cart': cart,
            'total': total
        }
        return render(request, 'orderTrack.html', context)
    else:
        cart = CartProducts.objects.filter(user=request.user)
        total = 0
        for rs in cart:
            if rs.item.discountPrice:
                total += rs.item.discountPrice * rs.quantity
            else:
                total += rs.item.price * rs.quantity
        context = {
            'Settings': setting,
            'cart': cart,
            'total': total
        }
        return render(request, 'orderTrack.html', context)


@login_required(login_url='/login')
def wishlist(request):
    setting = Settings.objects.get()
    if request.user.is_authenticated:
        cart = CartProducts.objects.filter(user=request.user)
        total = 0
        for rs in cart:
            if rs.item.discountPrice:
                total += rs.item.discountPrice * rs.quantity
            else:
                total += rs.item.price * rs.quantity
        context = {
            'Settings': setting,
            'cart': cart,
            'total': total
        }
        return render(request, 'wishlist.html', context)
    else:

        context = {
            'Settings': setting,
        }
        return render(request, 'wishlist.html', context)


def search(request):
    setting = Settings.objects.get()
    if request.user.is_authenticated:
        cart = CartProducts.objects.filter(user=request.user)
        total = 0
        for rs in cart:
            if rs.item.discountPrice:
                total += rs.item.discountPrice * rs.quantity
            else:
                total += rs.item.price * rs.quantity

        try:
            Search = request.GET.get('search')
        except:
            Search = None

        if Search:
            products = Products.objects.filter(name__icontains=Search)
            context = {'query': Search, 'Products': products, 'Settings': setting,
                       'cart': cart,
                       'total': total}
            template = 'result.html'
        else:
            template = 'shop.html'
            context = {
                'Settings': setting,
                'cart': cart,
                'total': total
            }
        return render(request, template, context)
    else:

        try:
            Search = request.GET.get('search')
        except:
            Search = None

        if Search:
            products = Products.objects.filter(name__icontains=Search)
            context = {'query': Search, 'Products': products, 'Settings': setting}
            template = 'result.html'
        else:
            template = 'shop.html'
            context = {
                'Settings': setting,

            }
        return render(request, template, context)


def CategoryNav(request):
    context = {}
    category = Categories.objects.raw("SELECT * FROM core_categories")
    return render(request, 'sideNav.html', {"Categories": category})


def notFound(request, exception):
    return render(request, 'base/404.html')


class shop(ListView):
    paginate_by = 4

    def get(self, request, *args, **kwargs):
        images = CarouselAdvImage.objects.get()
        product = Products.objects.all()
        setting = Settings.objects.get()
        categories = Categories.objects.all()
        if request.user.is_authenticated:
            cart = CartProducts.objects.filter(user=request.user)
            total = 0
            for rs in cart:
                if rs.item.discountPrice:
                    total += rs.item.discountPrice * rs.quantity
                else:
                    total += rs.item.price * rs.quantity
            context = {
                'Settings': setting,
                'cart': cart,
                'image': images,
                'categories': categories,
                'total': total, 'product': product,
            }
            return render(self.request, 'shop.html', context)
        else:
            context = {
                'Settings': setting,
                'image': images,
                'categories': categories,
                'product': product,
            }
            return render(self.request, 'shop.html', context)


class productDetail(DetailView):
    def get(self, request, *args, **kwargs):
        product = Products.objects.get(slug=self.kwargs['slug'])
        setting = Settings.objects.get()
        if request.user.is_authenticated:
            cart = CartProducts.objects.filter(user=request.user)
            total = 0
            for rs in cart:
                if rs.item.discountPrice:
                    total += rs.item.discountPrice * rs.quantity
                else:
                    total += rs.item.price * rs.quantity
            context = {
                'object': product,
                'Settings': setting,
                'cart': cart,
                'total': total
            }
            return render(self.request, "productDetail.html", context)
        else:
            context = {
                'object': product,
                'Settings': setting,
            }
            return render(self.request, "productDetail.html", context)


def home(request):
    product = Products.objects.all()
    setting = Settings.objects.get()
    images = CarouselAdvImage.objects.get()
    if request.user.is_authenticated:
        cart = CartProducts.objects.filter(user=request.user)
        total = 0
        for rs in cart:
            if rs.item.discountPrice:
                total += rs.item.discountPrice * rs.quantity
            else:
                total += rs.item.price * rs.quantity
        context = {
            'Settings': setting,
            'cart': cart,
            'image': images,
            'product': product,
            'total': total,
        }
        return render(request, 'home.html', context)
    else:
        context = {
            'Settings': setting,
            'image': images,
            'product': product,
        }
        return render(request, 'home.html', context)


# class home(ListView):
#     model = Products
#     template_name = "home.html"


class CategoryView(View):
    def get(self, request, *args, **kwargs):
        category = Categories.objects.get(slug=self.kwargs['slug'])
        item = Products.objects.filter(category=category, isactive=True)
        setting = Settings.objects.get()
        if request.user.is_authenticated:
            cart = CartProducts.objects.filter(user=request.user)
            total = 0
            for rs in cart:
                if rs.item.discountPrice:
                    total += rs.item.discountPrice * rs.quantity
                else:
                    total += rs.item.price * rs.quantity
            context = {
                'object_list': item,
                'category_title': category.name,
                'category_description': category.description,
                'category_image': category.image,
                'Settings': setting,
                'cart': cart,
                'total': total,

            }
            return render(self.request, "category.html", context)
        else:

            context = {
                'object_list': item,
                'category_title': category.name,
                'category_description': category.description,
                'category_image': category.image,
                'Settings': setting,

            }
            return render(self.request, "category.html", context)


class BrandView(View):
    def get(self, request, *args, **kwargs):
        brand = Brands.objects.get(slug=self.kwargs['slug'])
        item = Products.objects.filter(brand=brand, isactive=True)
        setting = Settings.objects.get()
        if request.user.is_authenticated:
            cart = CartProducts.objects.filter(user=request.user)
            total = 0
            for rs in cart:
                if rs.item.discountPrice:
                    total += rs.item.discountPrice * rs.quantity
                else:
                    total += rs.item.price * rs.quantity
            context = {
                'object_list': item,
                'Brand_title': brand.name,
                'Brand_description': brand.description,
                'Brand_image': brand.image,
                'Settings': setting,
                'cart': cart,
                'total': total,

            }
            return render(self.request, "brand.html", context)
        else:

            context = {
                'object_list': item,
                'Brand_title': brand.name,
                'Brand_description': brand.description,
                'Brand_image': brand.image,
                'Settings': setting,

            }
            return render(self.request, "brand.html", context)


@login_required(login_url='/login')
def add_to_cart(request, slug):
    item = get_object_or_404(Products, slug=slug)
    checkItem = CartProducts.objects.filter(user=request.user, item=item)
    if checkItem:
        control = 1
    else:
        control = 0

    if control == 1:  # Update  shopcart
        data = CartProducts.objects.get(item=item, user=request.user)
        data.quantity += 1
        data.save()
        messages.info(request, "Quantity was updated.")
    else:
        data = CartProducts()
        data.user = request.user
        data.item = item
        data.quantity = 1
        data.isOrdered = False
        data.save()
        messages.info(request, "Item was added to your cart.")

    return redirect("core:cart")


@login_required(login_url='/login')
def remove_single_item_from_cart(request, slug):
    item = get_object_or_404(Products, slug=slug)
    checkItem = CartProducts.objects.filter(user=request.user, item=item)
    if checkItem:
        control = 1
    else:
        control = 0

    if control == 1:  # Update  shopcart
        data = CartProducts.objects.get(item=item, user=request.user)
        if data.quantity > 1:
            data.quantity -= 1
            data.save()
            messages.info(request, "Quantity was updated.")
        else:
            item = get_object_or_404(Products, slug=slug)
            CartProducts.objects.filter(item=item).delete()
            messages.success(request, "Your item deleted form Cart.")

    return redirect("core:cart")


@login_required(login_url='/login')
def remove_from_cart(request, slug):
    item = get_object_or_404(Products, slug=slug)
    CartProducts.objects.filter(item=item).delete()
    messages.success(request, "Your item deleted form Cart.")
    return HttpResponseRedirect("/cart")


def storeList(request):
    seller = sellerProfile.objects.all()
    setting = Settings.objects.get()
    if request.user.is_authenticated:
        cart = CartProducts.objects.filter(user=request.user)
        total = 0
        for rs in cart:
            if rs.item.discountPrice:
                total += rs.item.discountPrice * rs.quantity
            else:
                total += rs.item.price * rs.quantity
        context = {
            'Settings': setting,
            'cart': cart,
            'total': total,
            'sellers': seller,
        }
        return render(request, 'storeList.html', context)
    else:
        context = {
            'Settings': setting,
            'sellers': seller,
        }
        return render(request, 'storeList.html', context)


class sellerDetails(View):
    def get(self, request, pk, *args, **kwargs):
        sellerUser = userProfile.objects.filter(id=self.kwargs['pk']).first()
        product = Products.objects.filter(user_id=sellerUser.id)
        setting = Settings.objects.get()
        if request.user.is_authenticated:
            cart = CartProducts.objects.filter(user=request.user)
            total = 0
            for rs in cart:
                if rs.item.discountPrice:
                    total += rs.item.discountPrice * rs.quantity
                else:
                    total += rs.item.price * rs.quantity
            context = {
                'product': product,
                'Settings': setting,
                'cart': cart,
                'total': total,
                'seller': sellerUser,
            }
            return render(self.request, "SellerDetails.html", context)
        else:
            context = {
                'product': product,
                'Settings': setting,
                'seller': sellerUser,
            }
            return render(self.request, "SellerDetails.html", context)
