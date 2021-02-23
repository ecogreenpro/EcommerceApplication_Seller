from django.urls import path
from . import views

from .views import (
    vandorOrderDetails, sellerDetails, sellerInfoReport, sellerRequestDetails,SellerDashboard,allProduct,addProduct

)

urlpatterns = [
    path('vendor-dashboard/', SellerDashboard.as_view(), name="vendorDashboard"),
    path('all-product/', allProduct.as_view(), name="allProduct"),
    path('add-new-product/', addProduct.as_view(), name="addProduct"),
    path('update-product/<slug>', views.updateProduct, name="updateProduct"),
    path('vendoer-stock-manager/', views.vendoerStockmanager, name="vendoerStockmanager"),
    path('vendoer-order-manager/', views.vendoerOrderManager, name="vendoerOrderManager"),
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
    path('seller-request-details/<pk>', sellerRequestDetails.as_view(), name="sellerRequestDetails"),
    path('seller-details/<Seller_id>', sellerDetails.as_view(), name="sellerDetails"),
    path('seller-report/<Seller_id>', sellerInfoReport.as_view(), name="sellerReport"),

    path('vandor-Order-Details/<order_Number>', vandorOrderDetails.as_view(), name="vandorOrderDetails"),

]
