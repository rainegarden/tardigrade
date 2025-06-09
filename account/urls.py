from django.urls import path
from . import views

urlpatterns = [
    path("pfp.png", views.render_pfp, name="render_pfp"),
    path("login/", views.login_view, name="login"),
]