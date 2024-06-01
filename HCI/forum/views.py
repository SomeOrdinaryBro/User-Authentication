from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm, LoginForm
from django.contrib.auth import login as auth_login, logout as auth_logout, authenticate
from django.contrib.auth.decorators import login_required

from django_ratelimit.decorators import ratelimit


@ratelimit(key='user_or_ip', rate='10/m')
def homepage(request):
    return render(request, 'forum/index.html')


@ratelimit(key='user_or_ip', rate='10/m')
def register(request):
    form = CustomUserCreationForm()

    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")

    context = {'registerform': form}
    return render(request, 'forum/register.html', context=context)


@ratelimit(key='user_or_ip', rate='10/m')
def login(request):
    form = LoginForm()

    if request.method == "POST":
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                auth_login(request, user)
                return redirect("dashboard")

    context = {'loginform': form}
    return render(request, 'forum/login.html', context=context)


@ratelimit(key='user_or_ip', rate='10/m')
@login_required(login_url="login")
def user_logout(request):
    auth_logout(request)
    return redirect("homepage")


@ratelimit(key='user_or_ip', rate='10/m')
@login_required(login_url="login")
def dashboard(request):
    return render(request, 'forum/dashboard.html')


@ratelimit(key='user_or_ip', rate='10/m')
@login_required(login_url="login")
def weather_app(request):
    return render(request, 'forum/apps/weather.html')
