# Create your views here.

from django.http import HttpRequest
from django.shortcuts import render


db = {
    1: {
        "title": "제목 1",
        "contents": "Post 1 body",
        "img": "https://picsum.photos/200/300",
    },
    2: {
        "title": "제목 2",
        "contents": "Post 2 body",
        "img": "https://picsum.photos/200/300",
    },
    3: {
        "title": "제목 3",
        "contents": "Post 3 body",
        "img": "https://picsum.photos/200/300",
    },
}


def blog(request: HttpRequest):
    return render(request, "blog.html", context={"db": db})


def post(request: HttpRequest, post_id: int):
    return render(request, "post.html", context={"post": db.get(post_id, None)})
