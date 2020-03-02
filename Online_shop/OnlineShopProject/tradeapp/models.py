from django.db import models
from django.contrib.auth.models import User
from django.contrib.postgres.fields import JSONField
from decimal import Decimal
from contentapp.models import Content
from loginapp.models import Address

class Cart(models.Model):
    """" Table for having the cart of each user, for each good order by each user save a single record"""
    on_cart = 'c'
    buy = 'b'
    status_cart = [(on_cart, 'c'), (buy, 'b')]
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='cart', related_query_name='carts')
    good = models.ForeignKey(Content,  on_delete=models.CASCADE)
    num = models.PositiveSmallIntegerField(default=1)
    status = models.CharField(max_length=10, choices=status_cart, default='c')
    date = models.DateField(auto_now=True)


class Order(models.Model):
    """" Table for saving the order of each user"""
    wait_for_confirm = 'wc'
    wait_for_buy = 'wb'
    buy = 'fb'
    Unverified = 'uv'
    verified = 'v'
    status_buy = [(wait_for_confirm, 'wc'), (wait_for_buy, 'wb'), (buy, 'fb')]
    status_supplier = [(Unverified, 'uv'), (verified, 'v')]
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user', related_query_name='users')
    goods = JSONField()
    address = models.ForeignKey(Address, on_delete=models.CASCADE, null=True)
    date = models.DateField(auto_now_add=True)
    payment_status = models.CharField(max_length=10, choices=status_buy, default='wc')
    supplier_status = models.CharField(max_length=10, choices=status_supplier, default='uv')

    @property
    def sum_price(self):
        sum_price = 0
        orders = self.goods
        for i in orders:
            sum_price += (Decimal(orders[i][1].strip(' "')) * orders[i][0]) # To Do: calculate according decimal
        return sum_price

