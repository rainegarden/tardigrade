from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect

from .forms import LoginForm
import hashlib

# Create your views here.

def get_gravitar(request):
    """
    Gets the gravitar hash from a request
    """
    if request.user.is_authenticated:
        return hashlib.sha256(request.user.email.lower().encode()).hexdigest()


def login_view(request):
    """
    Just a basic login view
    :param request:
    :return:
    """
    if request.user.is_authenticated:
        return redirect('/account')
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            # Authenticate
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("/account")
        # There was an error
        form = LoginForm()
        return render(request, 'account/login.html', {'form': form, "failed": "block"})
    form = LoginForm()
    return render(request, 'account/login.html', {'form': form, "failed": "none"})

def account_view(request):
    """
    Page for the account
    :param request:
    :return:
    """
    if not request.user.is_authenticated:
        return redirect('/account/login')
    return render(request, 'account/index.html', {"gravitar": get_gravitar(request)})

def logout_view(request):
    if request.user.is_authenticated:
        logout(request)
    return redirect('/account')