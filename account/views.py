from django.http import HttpResponse
from django.contrib.auth import authenticate
from django.shortcuts import render

from .forms import LoginForm
from .models import pfp

# Create your views here.
def render_pfp(request):
    """
    Render the profile from the binary data stored in the database to a png image.
    """
    if request.user.is_authenticated:
        user = request.user
        pfp  = pfp.objects.filter(user=user)
        if pfp.exists():
            pfp = pfp.first()
            return HttpResponse(pfp.image_binary, content_type='application/octet-stream')
        else:
            # If no profile picture exists, return a default image or None
            return HttpResponse('No profile found')
    else:
        return HttpResponse('No profile found')


def login_view(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            # Authenticate
            user = authenticate(request, username=username, password=password)
        else:
            form = LoginForm()
            return render(request, 'account/login.html', {'form': form, "failed": "block"})
    form = LoginForm()
    return render(request, 'account/login.html', {'form': form, "failed": "none"})