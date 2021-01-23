from django.urls import path
from django.conf.urls import handler400
from . import views

from .views import (
    allProduct

)

urlpatterns = [
    path('vendor-dashboard/', views.vendorDashboard, name="vendorDashboard"),
    #path('all-product/', views.allProduct, name="allProduct"),
    path('add-new-product/', views.addProduct, name="addProduct"),
    path('vendoer-stock-manager/', views.vendoerStockmanager, name="vendoerStockmanager"),
    path('vendoer-order-manager/', views.vendoerOrderManager, name="vendoerOrderManager"),
    path('vendoer-review-manager/', views.vendorReviewManager, name="vendorReviewManager"),
    path('vendoer-sales-report/', views.salesReport, name="salesReport"),
    path('vendoer-topSell-report/', views.topSelling, name="topSelling"),
    path('vendoer-accounts-report/', views.accountsReport, name="accountsReport"),
    path('become-seller/', views.becomeSeller, name="becomeSeller"),

    path('all-product/', allProduct.as_view(), name="allProduct")
]
