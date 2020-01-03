from django.urls import path
from .views import fetch_question_ravan,fetch_question_eghtesad,fetch_question_varzesh
urlpatterns = [
    path('ravanshenasi', fetch_question_ravan, name='fetch_question_ravan'),
    path('varzesh', fetch_question_varzesh, name='fetch_question_varzesh'),
    path('eghtesad', fetch_question_eghtesad, name='fetch_question_eghtesad')
]