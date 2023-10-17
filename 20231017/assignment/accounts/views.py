from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.http import HttpRequest
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView


# Create your views here.
class Register(CreateView):
    form_class = UserCreationForm
    template_name = "accounts/register.html"
    success_url = reverse_lazy("login")


class Login(LoginView):
    template_name = "accounts/login.html"
    next_page = "/"


class Logout(LoginRequiredMixin, LogoutView):
    template_name = "accounts/logout.html"
    next_page = "/"


@login_required
def profile(reqeust: HttpRequest):
    return render(reqeust, "accounts/profile.html", {"user": reqeust.user})
