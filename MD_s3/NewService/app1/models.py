from django.db import models


class Users(models.Model):
    name = models.CharField(max_length=200)
    level = models.BooleanField()


class News(models.Model):
    content = models.CharField(max_length=1000)
    data_submit_news = models.DateField(auto_now=True)
    news_writer = models.ForeignKey(Users, on_delete=models.CASCADE)

