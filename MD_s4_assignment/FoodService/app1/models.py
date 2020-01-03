from django.db import models


class User(models.Model):
    name = models.CharField(max_length=100)


class Food(models.Model):
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    price = models.IntegerField()


class CommentUser(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    food_id = models.ForeignKey(Food, on_delete=models.CASCADE)