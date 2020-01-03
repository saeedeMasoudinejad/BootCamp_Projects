from django.db import models


class Profile(models.Model):
    username = models.CharField(max_length=256)
    password = models.IntegerField()
    last_login = models.DateField(auto_now=True)
