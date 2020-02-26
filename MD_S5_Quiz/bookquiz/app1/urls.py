from django.urls import path
from django.views.decorators.csrf import csrf_exempt
from .views import*
urlpatterns = [
    path('books/', Show_book.as_view()),
    path('writer/', Show_writer.as_view()),
]