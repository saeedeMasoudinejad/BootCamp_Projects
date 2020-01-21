from django.db import models
from django.contrib.auth.models import User


class ProfileTable(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.IntegerField()
    birth_date = models.DateField(null=True)