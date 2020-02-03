from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from .serializer import CartSerializer, CartDetailSerializer
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Cart
from django.apps import apps
# from OnlineShopProject.contentapp.models import Content
# from contentapp.models
from contentapp.models import Content
from rest_framework.response import Response


class CartView(LoginRequiredMixin, ModelViewSet):
    """" Handel show cart of each user and add a goods in her cart"""
    # queryset = Cart.objects.all()
    def get_queryset(self):
        return Cart.objects.filter(user=self.request.user)

    def get_serializer_class(self):
        if self.action == 'list':
            return CartDetailSerializer
        else:
            return CartSerializer

class PayView(LoginRequiredMixin)
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