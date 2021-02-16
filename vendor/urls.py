from django.urls import path
from django.conf.urls import handler400
from . import views

from .views import (
    vandorOrderDetails, sellerDetails, sellerInfoReport

)

urlpatterns = [
    path('vendor-dashboard/', views.vendorDashboard, name="vendorDashboard"),
    path('all-product/', views.allProduct, name="allProduct"),
    path('add-new-product/', views.addProduct, name="addProduct"),
    path('update-product/<slug>', views.updateProduct, name="updateProduct"),
    path('vendoer-stock-manager/', views.vendoerStockmanager, name="vendoerStockmanager"),
    path('vendoer-order-manager/', views.vendoerOrderManager, name="vendoerOrderManager"),
    # path('Update-order/', views.updateOrder, name="updateOrder"),
    path('vendoer-review-manager/', views.vendorReviewManager, name="vendorReviewManager"),
    path('vendoer-sales-report/', views.salesReport, name="salesReport"),
    path('vendoer-topSell-report/', views.topSelling, name="topSelling"),
    path('vendoer-accounts-report/', views.accountsReport, name="accountsReport"),
    path('become-seller/', views.becomeSeller, name="becomeSeller"),
    path('seller-profile/', views.settings, name="sellerProfile"),
    path('seller-update/', views.sellerUpdate, name="sellerUpdate"),
    path('seller-change-password/', views.sellerChangePassword, name="sellerChangePassword"),
    path('Jewellery-sellers/', views.allSeller, name="allSeller"),
    path('seller-request/', views.sellerRequest, name="sellerRequest"),
    path('seller-details/<Seller_id>', sellerDetails.as_view(), name="sellerDetails"),
    path('seller-report/<Seller_id>', sellerInfoReport.as_view(), name="sellerReport"),

    path('vandor-Order-Details/<order_Number>', vandorOrderDetails.as_view(), name="vandorOrderDetails"),

]
