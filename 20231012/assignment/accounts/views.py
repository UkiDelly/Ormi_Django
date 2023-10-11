from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.http import HttpRequest
from django.shortcuts import render
from django.views.generic import CreateView

# Create your views here.

sign_up = CreateView.as_view(
    form_class=UserCreationForm,
    template_name="accounts/signup.html",
    success_url="/blog/",
)

login = LoginView.as_view(
    template_name="accounts/login.html",
    success_url="/blog/",
    next_page="/blog/",
)

logout = LogoutView.as_view(
    next_page="/blog/",
)


@login_required
def profile(request: HttpRequest):
    return render(request, "accounts/profile.html")
