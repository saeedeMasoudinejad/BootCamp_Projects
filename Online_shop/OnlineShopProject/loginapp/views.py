from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.forms import UserCreationForm
from .froms import ProfileForm
from .models import ProfileTable
from django.contrib.auth.views import LoginView
from django.http import HttpResponse
from django.contrib.auth.models import User
# from django.contrib.auth.views import

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
            return redirect('home')
        else:
            return HttpResponse("Not valid")


class Profile(View):

    def get(self, request):
        profile_form = ProfileForm()
        return render(request, 'profile.html', {'profile_form': profile_form})

    def post(self, request):
        profile_data_form = ProfileForm(request.POST)
        if profile_data_form.is_valid():
            first_name = profile_data_form.cleaned_data['first_name']
            last_name = profile_data_form.cleaned_data['last_name']
            email = profile_data_form.cleaned_data['email']
            mobile = profile_data_form.cleaned_data['mobile']
            # birth_date = profile_data_form.cleaned_data['birth_date']
            user = User.objects.get(username=request.user)
            user.first_name = first_name
            user.last_name = last_name
            user.email = email
            user.save()
            profile = ProfileTable(user=user, phone_number=mobile)
            profile.save()