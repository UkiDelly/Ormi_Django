from django.http import HttpRequest
from django.shortcuts import render

from .models import Post


# Create your views here.
def blog(request: HttpRequest):
    posts = Post.objects.all()

    return render(request, "blog/blog.html", {"db": posts})


def post(request: HttpRequest, post_id: int):
    # try:
    post = Post.objects.get(pk=post_id)
    # except Post.DoesNotExist:
    #     return JsonResponse({"error": "Post not found"}, status=404)
    # print(post)
    context = {"post": post}
    return render(request, "blog/post.html", context)
    # return JsonResponse(post.to_json())


def test(request: HttpRequest):
    ...
