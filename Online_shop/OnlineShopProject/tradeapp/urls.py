from django.urls import path,include
from .views import CartView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('cart', CartView, basename='cart_list')
router.register('pay', PayView)
urlpatterns = [
    # path('cart/', CartView.as_view())
    path('finance', include(router.urls)),

]
