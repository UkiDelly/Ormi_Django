from django.http import HttpRequest
from django.shortcuts import render


# Create your views here.
def blog(request: HttpRequest):
    return render(request, "blog/blog.html")


def post(request: HttpRequest, post_id: int):
    context = {"post_id": post_id}
    return render(request, "blog/post.html", context)
