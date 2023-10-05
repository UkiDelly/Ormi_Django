from django.http import HttpRequest
from django.shortcuts import render


# Create your views here.
def login(request: HttpRequest):
    return render(request, "login.html")


def logout(request: HttpRequest):
    return render(request, "logout.html")
