from django.urls import path, include
from . import views
from .views import SignUp, Profile
# from OnlineShopProject.contentapp import urls
urlpatterns = [
    path('home/', views.load_main_page, name='home'),
    path('signup/', SignUp.as_view(), name='register'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('profile/', Profile.as_view(), name='profile'),

]