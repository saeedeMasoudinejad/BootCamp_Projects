from django.urls import path, include
from . import views
from .views import SignUp, Profile
from django.views.decorators.csrf import csrf_exempt
# from OnlineShopProject.contentapp import urls
urlpatterns = [
    path('home/', views.load_main_page, name='home'),
    path('signup/', SignUp.as_view(), name='register'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('profile/', csrf_exempt(Profile.as_view()), name='profile'),

]