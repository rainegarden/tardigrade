from django.urls import path
from . import views

urlpatterns = [
    path("login/", views.login_view, name="login"),
    path("", views.account_view, name="account_view"),
    path("logout/", views.logout_view, name="logout"),
]