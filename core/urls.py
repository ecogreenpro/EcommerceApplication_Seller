from django.urls import path

from . import views
from .views import (
    productDetail,
    shop,
    home,
    CategoryView,
    add_to_cart,
    # CartView,
    # checkoutView,
    BrandView,
    remove_from_cart,
    remove_single_item_from_cart, invoiceView, sellerDetails

)

app_name = 'core'
urlpatterns = [
    path('', views.home, name="home"),
    path('search/', views.search, name="search"),
    path('header/', views.header, name="header"),
    path('about/', views.about, name="about"),
    path('contact/', views.contact, name="contact"),
    path('privacy/', views.privacyPolicy, name="privacyPolicy"),
    path('payment-process/', views.paymentProcess, name="paymentProcess"),
    path('checkout/', views.checkout, name="checkout"),
    path('cart/', views.cart, name="cart"),
    path('refund-returns-policy/', views.terms, name="refundReturnsPolicy"),
    path('order-track/', views.orderTrack, name="orderTrack"),
    # path('wishlist/', views.wishlist, name="wishlist"),
    path('add-to-cart/<slug>/', add_to_cart, name='add-to-cart'),
    path('remove-from-cart/<slug>/', remove_from_cart, name='remove-from-cart'),
    path('remove-single-item-cart/<slug>/', remove_single_item_from_cart, name='remove-single-from-cart'),
    # path('become-seller/', views.becomeSeller, name="becomeSeller"),
    path('login/', views.login, name="login"),
    path('logout/', views.logout, name="logout"),
    # path('dashboard/', views.dashboard, name="dashboard"),
    path('signup/', views.signup, name="signup"),
    path('create-user/', views.createUser, name="createUser"),
    path('forgotpassword/', views.forgotpassword, name="forgotpassword"),
    path('change-password/', views.changePassword, name="changePassword"),
    path('user-profile/', views.userprofile, name="userprofile"),
    path('update-Profile/', views.updateProfile, name="updateProfile"),
    path('userorder/', views.userOrder, name="userOrder"),
    path('jewelry-store/', views.storeList, name="storeList"),
    path('invoice/<order_Number>/', invoiceView.as_view(), name='invoice'),
    path('jewelry-seller/<Seller_id>/', sellerDetails.as_view(), name='sellerDetails'),
    path('chat/', views.chat, name="chat"),
    path('shop/', shop.as_view(), name='shop'),
    path('product/<slug>/', productDetail.as_view(), name='productDetail'),
    path('category/<slug>/', CategoryView.as_view(), name='category'),
    path('brand/<slug>/', BrandView.as_view(), name='brand'),


]
