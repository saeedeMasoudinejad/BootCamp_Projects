from django.urls import path
from .views import*
from django.views.decorators.csrf import csrf_exempt
urlpatterns = [
    path('login/', loginshow),
    path('validations/', csrf_exempt(check), name='checking')

]