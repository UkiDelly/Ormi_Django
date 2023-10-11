from django.http import HttpRequest
from django.shortcuts import render


# Create your views here.
def index(request: HttpRequest):
    return render(request, "main/index.html")


def about(request: HttpRequest):
    return render(request, "main/about.html")


def contact(request: HttpRequest):
    return render(request, "main/contact.html")
