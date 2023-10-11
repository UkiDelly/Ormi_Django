from django.conf import settings
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.views.generic import CreateView

# Create your views here.
# Class 기반 뷰로 구현

signup = CreateView.as_view(
    form_class=UserCreationForm,
    template_name="accounts/html",
    success_url=settings.LOGIN_URL,
)

login = LoginView.as_view(
    template_name="accounts/form.html", success_url="/accounts/profile"
)

logout = LogoutView.as_view(next_page=settings.LOGOUT_URL)


@login_required
def profile(request: HttpRequest):
    return render(request, "accounts/profile.html")


def login_check(request: HttpRequest):
    return render(request, "accounts/logincheck.html")


def loginfbv(request: HttpRequest):
    if request.method == "POST":
        username, password = request.POST["username"], request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponse("Login Success")
        else:
            return HttpResponse("Login Failed")

    return render(request, "accounts/loginfbv.html")
