from django.shortcuts import render
from django.views import View
from django.http import JsonResponse
from .models import Profile
# class LoginShow(View):
#     render('index.html')


def loginshow(request):
    return render(request, 'index.html')


def check(request):
    # with the method of GET
    # username = request.GET['username']
    # password = request.GET['pass']
    # find_person = Profile.objects.filter(username=username, password=password)
    # if len(find_person) > 0:
    #     result = {'validation': 'login successfully'}
    # else:
    #     result = {'Error': 'username or password is not correct'}
    # return render(request, 'validationshow.html', {'result': result})
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['pass']
        find_person = Profile.objects.filter(username=username, password=password)
        if len(find_person) > 0:
            # result = {'validation': 'login successfully'}
            result = 1
        else:
            # result = {'Error': 'username or password is not correct'}
            result = 0
        return render(request, 'validationshow.html', {'result': result})