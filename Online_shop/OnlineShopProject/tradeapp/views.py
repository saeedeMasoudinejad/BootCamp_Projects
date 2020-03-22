from django.shortcuts import render, redirect
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet
from .serializer import CartSerializer, CartDetailSerializer, OrderSerializer, ChoiceAddressSerializer,\
    FinalFactorSerializer, PaymentSerializer, SupplierSerializer
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from .models import Cart, Order
from contentapp.models import Content
from loginapp.models import Address
from loginapp.serializer import AddressSerializer
from rest_framework.response import Response
from django.http import HttpResponse
from django.apps import apps
# from OnlineShopProject.contentapp.models import Content
# from contentapp.models


class CartView(LoginRequiredMixin, ModelViewSet):
    """" Handel show cart of each user and add,update and delete a goods"""
    def get_queryset(self):
        return Cart.objects.filter(user=self.request.user, status='c')

    def get_serializer_class(self):
        if self.action == 'list':
            return CartDetailSerializer
        else:
            return CartSerializer


class OrderView(LoginRequiredMixin, ModelViewSet):
    """" Handel the payment process of order each user"""

    def get_queryset(self):
        return Cart.objects.filter(user=self.request.user, status='c')

    def get_serializer_class(self):
        if self.action == 'list':
            return CartDetailSerializer
        else:
            return OrderSerializer

    def create(self, request):
        serializer_data = self.get_serializer(data=request.data)
        user_orders = {}
        if serializer_data.is_valid():
            confirm_status = serializer_data.validated_data.get('confirmation_status')
            not_exist_good = False
            if confirm_status == 'confirm':
                user_cart = Cart.objects.filter(user=self.request.user, status='c')
                for i in user_cart:
                    if i.good.inventory >= i.num:
                        user_orders[i.good.name] = (i.num, str(i.good.price))
                    elif i.good.inventory < i.num and i.good.inventory != 0:
                        not_exist_good = True
                        return Response('{} exist just {} in store but you want {}, please update the number you want '
                                        'or delete this good from your cart'.
                                        format(i.good.name, i.good.inventory, i.num))
                    else:
                        not_exist_good = True
                        return Response('{} doesn\'t exist in store, please delete this good from your cart'
                                        .format(i.good.name))
                if not not_exist_good:
                    user_order_exist = Order.objects.filter(user=request.user, payment_status='wc').first()
                    if user_order_exist is not None:
                        user_order_exist.goods = user_orders
                        user_order_exist.save()
                    else:
                        Order(user=request.user, goods=user_orders).save()
                    return redirect('/finance/address')  # To Do: go to next step of buying show the address


class AddressView(LoginRequiredMixin,ModelViewSet):
    """" show and select the address """
    def get_queryset(self):
        return Address.objects.filter(user=self.request.user)

    def get_serializer_class(self):
        if self.action == 'list':
            return AddressSerializer
        else:
            return ChoiceAddressSerializer

    # serializer_class = AddressSerializer

    def create(self, request):
        serializer_data = self.get_serializer(data=request.data)
        if serializer_data.is_valid():
            address_id = serializer_data.validated_data.get('address_id')
            if Address.objects.get(id=address_id).user == request.user:
                user_order = Order.objects.get(user=request.user, payment_status='wc')
                print(user_order)
                user_order.address = Address.objects.get(id=address_id)
                user_order.save()
                return redirect('/finance/showfinalfactor/')
            else:
                return Response("The address you chose is not valid for you")
        else:
            return Response("Should choice one of the address id it's show you")


class AddAddressView(ModelViewSet):
    def get_queryset(self):
        return Address.objects.filter(user= self.request.user)
    serializer_class = AddressSerializer


class FactorView(LoginRequiredMixin,ReadOnlyModelViewSet):
    def get_queryset(self):
        return Order.objects.filter(user=self.request.user, payment_status='wc')

    def get_serializer_class(self):
        if self.action == 'list':
            return FinalFactorSerializer
        else:
            return PaymentSerializer

    def create(self, request):
        serilaizer_data = self.get_serializer(data=request.data)
        if serilaizer_data.is_valid():
            if serilaizer_data.validated_data.get('confirmation_status') == 'pay':
                user_factor = Order.objects.get(user=request.user, payment_status='wc')
                """ because don't get a request from bank api chang status to fb otherwise should change to
                 wb and when get successful payment response from bank api change to fb """
                user_factor.payment_status = 'fb'
                user_factor.save()
                user_order = Cart.objects.filter(user=request.user, status='c')
                for u in user_order:
                    u.good.inventory -= u.num
                    u.good.save()
                    u.delete()
                return Response("Your order is complete")
            else:
                return redirect('/finance/cart/')


class ShowAllBuy(LoginRequiredMixin,ReadOnlyModelViewSet):
    def get_queryset(self):
        return Order.objects.filter(user=self.request.user, payment_status='fb')

    serializer_class = FinalFactorSerializer

class SupplierView(LoginRequiredMixin, ModelViewSet):
    permission_required = ('User.Can watch factor')

    def get_queryset(self):
        return Order.objects.filter(payment_status='fb', supplier_status='uv')

    def get_serializer_class(self):
        if self.action == 'list':
            return FinalFactorSerializer
        else:
            return SupplierSerializer


    # def perform_create(self, serializer):
    #     instance = serializer.save()
    #     print(instance['confirmation_status'])
    #     if instance['confirmation_status'] == 'confirm':
    #         print("True")
    #         user_cart = Cart.objects.filter(user=self.request.user, status='c')
    #         print(user_cart)
    #         for i in user_cart:
    #             print(i)
    #             if i.good.inventory >= i.num:
    #                 print(i.good.inventory)
    #                 i.good.inventory -= i.num
    #                 print(i.good.inventory)
    #                 i.status = 'b'
    #                 i.save()
    #                 i.good.save()
    #             else:
    #                 print("##############")
    #                 return redirect('finance/cart/')



    # def get_queryset(self):
    #     return Cart.objects.filter(user=self.request.user)

    # authentication_classes = (TokenAuthentication,)
    # permission_classes = (IsAuthenticated,)

    # def post(self, request):
    #     """ set the good and number in Cart of user"""
    #     value_new_item = self.serializer_class(data=request.data)
    #     if value_new_item.is_valid():
    #         good_id = value_new_item.validated_data.get('good_id')
    #         good_num = value_new_item.validated_data.get('num')
    #         good_obj = Content.objects.get(id=good_id)
    #         if good_obj.inventory >= good_num:
    #             exist_user_good = Cart.objects.get(user=request.user, good=good_obj, status='c')
    #             print(exist_user_good)
    #             if exist_user_good is None:
    #                 Cart(user=request.user, good=Content.objects.get(id=good_id), num=good_num).save()
    #                 good_obj.inventory -= good_num
    #                 good_obj.save()
    #             else:
    #                 exist_user_good.num += good_num
    #                 exist_user_good.save()
    #         else:
    #             return Response("This good is not enough exist")

    # def get(self, request, serializer):
    #     instance = serializer.save()
    #     return Response(instance)