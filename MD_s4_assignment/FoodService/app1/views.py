from django.shortcuts import render
from django.views.generic import ListView
# from django.views.generic import TemplateView
from .models import User, Food, CommentUser


class MyTemplateShow(ListView):
    model = User
    template_name = 'page.html'

    def get_context_data(self, **kwargs):  # To DO check the objectlist argumant
        context = super().get_context_data(**kwargs)
        context['Food_data'] = Food.objects.all()
        context['Comment_data'] = CommentUser.objects.all()
        return context