from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType

class ProfileTable(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=256)
    birth_date = models.DateField(null=True)


class Address(models.Model):
    """ save all address of each user"""
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='address_user')
    city = models.CharField(max_length=256)
    address = models.TextField()
    zip_number = models.CharField(max_length=256)


""" create the new permission for supplier"""
try:
    content_type = ContentType.objects.get(app_label='auth', model='user')
    permission = Permission.objects.create(codename='can_watch_factor', name='Can watch factor',
                                           content_type=content_type)
except:
    pass