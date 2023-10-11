from django.http import HttpRequest
from django.shortcuts import get_object_or_404, redirect, render
from django.db.models import Q

from .form import PostForm
from .models import Post


def blog(request: HttpRequest):
    if request.GET.get("q"):
        q = request.GET.get("q")
        db = Post.objects.filter(
            Q(title__icontains=q) | Q(contents__icontains=q)
        ).distinct()
    else:
        db = Post.objects.all()
    context = {"db": db}
    return render(request, "blog/blog.html", context)


def post(request: HttpRequest, pk: int):
    db = Post.objects.get(pk=pk)
    context = {
        "db": db,
    }
    return render(request, "blog/post.html", context)


def create(request: HttpRequest):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)  # 수정
        if form.is_valid():
            post: Post = form.save()
            return redirect("post", pk=post.pk)
    else:
        form = PostForm()
    return render(request, "blog/create.html", {"form": form})


def update(request: HttpRequest, pk: int):
    post = get_object_or_404(Post, pk=pk)
    
    # print(post) # 없는 페이지와 있는 페이지를 모두 테스트 해보세요.
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES, instance=post)  # 수정
        if form.is_valid():
            post = form.save()
            return redirect("blog")
    else:
        form = PostForm(instance=post)
    return render(request, "blog/create.html", {"form": form})


def delete(request: HttpRequest, pk: int):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        post.delete()
        return redirect("blog")
    return render(request, "blog/delete.html", {"post": post})
