from django.db import models
from django.contrib.auth.models import User
from django.apps import apps
from contentapp.models import Content


class Cart(models.Model):
    """" Table for having the cart of each user, for each good order by each user save a single record"""
    on_cart = 'c'
    buy = 'b'
    status_cart = [(on_cart, 'c'), (buy, 'b')]
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='cart', related_query_name='carts')
    good = models.ForeignKey(Content,  on_delete=models.CASCADE)
    num = models.PositiveSmallIntegerField(default=1)
    status = models.CharField(max_length=10, choices=status_cart, default='c')


