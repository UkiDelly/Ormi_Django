from django.http import HttpRequest
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import (
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)

from blog.models import Post, CommentForm, Comment


# Create your views here.


def posts(request: HttpRequest):
    posts = Post.objects.filter(created_at__month=10)
    request.user.first_name
    return render(request, "blog/post_list.html", {"posts": posts})


def tags(requst: HttpRequest, tag: str):
    posts = Post.objects.filter(tags__name__iexact=tag)
    return render(requst, "blog/post_list.html", {"posts": posts})


class PostDetail(DetailView):
    model = Post


def post_detail(request: HttpRequest, pk: int):
    post = Post.objects.get(pk=pk)
    form = CommentForm()

    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            c = Comment.objects.create(
                message=form.cleaned_data["message"], post=post, author=request.user
            )

            c.save()
    return render(request, "blog/post_detail.html", {"post": post, "form": form})


class PostCreate(CreateView):
    model = Post
    fields = "__all__"
    success_url = reverse_lazy("postlist")


class PostUpdate(UpdateView):
    model = Post
    fields = "__all__"
    success_url = reverse_lazy("postlist")


class PostDelete(DeleteView):
    model = Post
    success_url = reverse_lazy(
        "postlist"
    )  # 삭제되고 처리가 다 완료되지 않았을 수 있으니 지연 필요한 reverse_lazy를 사용함.
