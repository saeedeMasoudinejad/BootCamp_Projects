from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=256)
    birth_date = models.DateField()


class AllQuestion(models.Model):
    question = models.TextField()
    first_choice = models.TextField()
    secound_choice = models.TextField()
    third_choice = models.TextField()
    fourth_choice = models.TextField()
    correct_answer = models.TextField()
    profile = models.ManyToManyField(Profile)


class QuestionUser(models.Model):
    user_id = models.CharField(max_length=256)
    questions_id = models.CharField(max_length=256)
