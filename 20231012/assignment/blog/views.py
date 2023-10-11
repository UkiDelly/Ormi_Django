from django.contrib.auth.decorators import login_required
from django.http import HttpRequest, HttpResponseNotFound, Http404
from django.shortcuts import redirect, render, get_object_or_404
from django.views.generic import CreateView

from .models import Post, PostForm


# Create your views here.


def blog(request: HttpRequest):
    posts = Post.objects.all()
    return render(request, "blog/blog.html", {"posts": posts})


create_post = CreateView.as_view(
    form_class=PostForm,
    template_name="blog/create.html",
    success_url="/blog/",
)


@login_required()
def create_post(request: HttpRequest):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("blog")
    else:
        form = PostForm()
    return render(request, "blog/create.html", {"form": form})


def post(request: HttpRequest, pk: int):
    try:
        post = get_object_or_404(Post, pk=pk)
    except Http404:
        return HttpResponseNotFound("<h1>Post does not exist</h1>")
    return render(request, "blog/post.html", {"post": post})


@login_required()
def update_post(request: HttpRequest, pk: int):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect("blog")
    else:
        form = PostForm(instance=post)
    return render(request, "blog/create.html.html", {"form": form})


@login_required()
def delete_post(request: HttpRequest, pk: int):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        post.delete()
        return redirect("blog")
    return render(request, "blog/delete.html", {"post": post})
