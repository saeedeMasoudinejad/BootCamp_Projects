from django.db import models

from django.db import models


class Category(models.Model):
    name_category = models.CharField(max_length=256)

    def __str__(self):
        return self.name_category


class SubCategory(models.Model):
    name_sub = models.CharField(max_length=256)
    name_cat = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='cat')

    def __str__(self):
        return self.name_sub


class Brand(models.Model):
    name_brand = models.CharField(max_length=256)

    def __str__(self):
        return self.name_brand


class Type(models.Model):
    type_name = models.CharField(max_length=256)

    def __str__(self):
        return self.type_name


class Content(models.Model):
    name = models.CharField(max_length=256)
    price = models.IntegerField()

    def __str__(self):
        return self.name


class Mobile(Content):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    img = models.ImageField()
    weight = models.IntegerField()
    ram = models.IntegerField()
    camera = models.BooleanField()

    def __str__(self):
        return self.name


class TV(Content):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    sub_category = models.ForeignKey(SubCategory, on_delete=models.CASCADE, null=True)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    img = models.ImageField()
    weight = models.IntegerField()
    dimensions = models.CharField(max_length=256)
    hdmi = models.BooleanField()

    def __str__(self):
        return self.name


class Laptop(Content):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    img = models.ImageField()
    weight = models.IntegerField()
    cpu = models.CharField(max_length=256)
    cache = models.IntegerField()
    webcame = models.BooleanField()

    def __str__(self):
        return self.name


class Refrigerator(Content):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    sub_category = models.ForeignKey(SubCategory, on_delete=models.CASCADE, null=True)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    img = models.ImageField()
    capacity = models.IntegerField()
    floor_number = models.IntegerField()

    def __str__(self):
        return self.name
