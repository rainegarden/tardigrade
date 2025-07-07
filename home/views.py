from django.shortcuts import render, redirect
from account.views import get_gravitar
# Create your views here.
def home(request):
    if request.user.is_authenticated:
        return render(request, "index.html", {"gravitar": get_gravitar(request)})
    return redirect("/account/login")
