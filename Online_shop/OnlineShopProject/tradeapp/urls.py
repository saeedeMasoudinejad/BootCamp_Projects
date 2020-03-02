from django.urls import path, include
from .views import CartView, OrderView, AddressView, FactorView, SupplierView, AddAddressView, ShowAllBuy
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('cart', CartView, basename='cart_list')
# router.register('cart/<int:id>/', CartView, basename='cart_list')
router.register('order', OrderView, basename='pay_list')
router.register('address', AddressView, basename='ad_list')
router.register('showfinalfactor', FactorView, basename='factor')
router.register('showAllBuy', ShowAllBuy, basename='b')
router.register('factors', SupplierView, basename='f')
router.register('add_address', AddAddressView, basename='add_address')
urlpatterns = [
    # path('cart/', CartView.as_view())
    path('finance/', include(router.urls)),

]
