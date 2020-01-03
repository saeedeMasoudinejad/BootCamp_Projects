from django.db import models


class Questions(models.Model):
    category = models.CharField(max_length=200)
    content = models.CharField(max_length=500)
