from django.shortcuts import render, redirect
from django.views import View
from .models import ProfileTable, Address
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin


def load_main_page(request):
    return render(request, 'base.html')


class SignUp(View):

    def get(self, request):
        signup_form = UserCreationForm()
        return render(request, 'signup.html', {'signup_form': signup_form})

    def post(self, request):
        form_data = UserCreationForm(request.POST)
        if form_data.is_valid():
            form_data.save()
            result = 1
            # user = authenticate(request, username=request.POST['username'], password=request.POST['password1'])
            # Token.objects.get_or_create(user=user)
            return redirect('/accounts/login/')
        else:
            result = 0
            return render(request, 'validationshow.html', {'result': result})


class Profile(LoginRequiredMixin, View):

    def get(self, request):
        return render(request, 'profile.html')

    def post(self, request):
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        mobile = request.POST['mobile']
        city = request.POST['city']
        zip = request.POST['zip']
        address = request.POST['address']
        user = User.objects.get(username=request.user)
        user.first_name = first_name
        user.last_name = last_name
        user.email = email
        user.save()
        profile = ProfileTable(user=user, phone_number=mobile)
        profile.save()
        address = Address(user=user, city=city, address=address, zip_number=zip)
        address.save()
        return redirect('/home')