from django.db import models
from model_utils.managers import InheritanceManager

class Category(models.Model):
    name_category = models.CharField(max_length=256, verbose_name="نام دسته")

    def __str__(self):
        return self.name_category


class SubCategory(models.Model):
    name_sub = models.CharField(max_length=256, verbose_name="نام زیر دسته")
    name_cat = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='cat')

    def __str__(self):
        return self.name_sub


class Brand(models.Model):
    name_brand = models.CharField(max_length=256, verbose_name="نام برند")

    def __str__(self):
        return self.name_brand


class Type(models.Model):
    type_name = models.CharField(max_length=256)

    def __str__(self):
        return self.type_name


class Content(models.Model):
    """ This model is a parent of all type of products is exists in shop like laptop and eth"""
    name = models.CharField(max_length=256, verbose_name="نام محصول")
    price = models.DecimalField(max_digits=10, decimal_places=3, help_text="ریال", verbose_name="قیمت")
    inventory = models.PositiveIntegerField("تعداد موجود")
    img = models.ImageField(verbose_name="تصویر محصول")
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, verbose_name="نام برند")

    @property
    def existance_status(self):
        if self.inventory > 0:
            status = 'موحود'
        else:
            status = 'ناموجود'
        return status

    def __str__(self):
        return self.name


class Mobile(Content):
    # silver = 'silver'
    # black = 'black'
    # rosegold = 'rosegold'
    # white = 'white'
    # mobile_color = [
    #     (silver, 'silver'),
    #     (black, 'black'),
    #     (rosegold, 'rosegold'),
    #     (white, 'white')
    # ]
    parent_link = models.OneToOneField(Content, on_delete=models.CASCADE, parent_link=True, related_name='mobile')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="نام دسته")
    weight = models.FloatField(help_text="according of kg", verbose_name="وزن")
    ram = models.IntegerField(help_text="according of GB")
    # color = models.CharField(choices=mobile_color, max_length=50, verbose_name="رنگ")
    camera = models.BooleanField(verbose_name="دارای دوربین است")

    def __str__(self):
        return self.name


class TV(Content):
    parent_link = models.OneToOneField(Content, on_delete=models.CASCADE, parent_link=True, related_name='tv')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="نام دسته")
    sub_category = models.ForeignKey(SubCategory, on_delete=models.CASCADE, null=True, verbose_name="نام زیر دسته")
    weight = models.FloatField(help_text="according of kg", verbose_name="وزن")
    dimensions = models.CharField(max_length=256, help_text="according of this pattern a*b*c", verbose_name="ابعاد")
    hdmi = models.BooleanField(verbose_name="دارای پورت hdmi")

    def __str__(self):
        return self.name


class Laptop(Content):
    parent_link = models.OneToOneField(Content, on_delete=models.CASCADE, parent_link=True, related_name='laptop')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="نام دسته")
    weight = models.FloatField(help_text="according of kg", verbose_name="وزن")
    cpu = models.CharField(max_length=256)
    cache = models.IntegerField(help_text="according of MB")
    webcame = models.BooleanField(verbose_name="دارای وب کم هست")

    def __str__(self):
        return self.name


class Refrigerator(Content):
    parent_link = models.OneToOneField(Content, on_delete=models.CASCADE, parent_link=True, related_name='ref')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="نام دسته")
    sub_category = models.ForeignKey(SubCategory, on_delete=models.CASCADE, null=True, verbose_name="نام زیر دسته")
    capacity = models.FloatField(help_text="according of kg", verbose_name="ظرفیت یخچال")
    floor_number = models.IntegerField(verbose_name="تعداد طبقات")

    def __str__(self):
        return self.name
