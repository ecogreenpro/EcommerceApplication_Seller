from django.urls import path
from django.conf.urls import handler400
from . import views

from .views import (
    allProduct, vandorOrderDetails

)

urlpatterns = [
    path('vendor-dashboard/', views.vendorDashboard, name="vendorDashboard"),
    # path('all-product/', views.allProduct, name="allProduct"),
    path('add-new-product/', views.addProduct, name="addProduct"),
    path('vendoer-stock-manager/', views.vendoerStockmanager, name="vendoerStockmanager"),
    path('vendoer-order-manager/', views.vendoerOrderManager, name="vendoerOrderManager"),
    #path('Update-order/', views.updateOrder, name="updateOrder"),
    path('vendoer-review-manager/', views.vendorReviewManager, name="vendorReviewManager"),
    path('vendoer-sales-report/', views.salesReport, name="salesReport"),
    path('vendoer-topSell-report/', views.topSelling, name="topSelling"),
    path('vendoer-accounts-report/', views.accountsReport, name="accountsReport"),
    path('become-seller/', views.becomeSeller, name="becomeSeller"),
    # path('update-order/<order_Number>', views.vandorUpdateOrder, name="updateOrder"),

    path('all-product/', allProduct.as_view(), name="allProduct"),
    path('vandor-Order-Details/<order_Number>', vandorOrderDetails.as_view(), name="vandorOrderDetails")
]
