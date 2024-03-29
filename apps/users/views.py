from django.shortcuts import render
from django.contrib.auth import authenticate, login
# from django.views.generic.base import View
from django.db.models import Q


# Create your views here.

def user_login(request):
    if request.method == "GET":
        return render(request, 'login.html', {})

    elif request.method == 'POST':
        user_name = request.POST.get('username', '')
        pass_word = request.POST.get('password', '')
        # 认证,通过返回对象，不通过 返回None
        user = authenticate(username=user_name, password=pass_word)
        if user is not None:
            login(request, user)
            return render(request, 'index.html')
        else:
            return render(request, 'login.html', {})


def user_register(request):
    return render(request, 'register.html', {})


def user_forgetpwd(request):
    if request.method == 'GET':
        return render(request, 'forgetpwd.html', {})
