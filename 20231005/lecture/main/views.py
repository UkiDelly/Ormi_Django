from django.http import HttpRequest
from django.shortcuts import render


# Create your views here.
def index(request: HttpRequest):
    return render(request, "index.html")


def about(request: HttpRequest):
    return render(request, "about.html")


def contact(request: HttpRequest):
    return render(request, "contact.html")
