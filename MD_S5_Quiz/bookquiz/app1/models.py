from django.db import models


class Writer(models.Model):
    name = models.CharField(max_length=300)
    def __str__(self):
        return self.name

class Book(models.Model):
    name = models.CharField(max_length=500)
    chap = models.DateField()
    inter_exter = models.BooleanField()
    translator = models.CharField(max_length=200, blank=True)
    wirter = models.ManyToManyField(Writer, related_name='books', related_query_name='book')
    def __str__(self):
        return self.name