from django.urls import path
from .views import*
from django.views.decorators.csrf import csrf_exempt
urlpatterns = [
    path('quiz/<str:username>', csrf_exempt(QuizView.as_view())),
    path('quiz/', csrf_exempt(QuizView.as_view())),
]