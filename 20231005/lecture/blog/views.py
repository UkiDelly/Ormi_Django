import json
from bs4 import BeautifulSoup
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
import requests

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


# Create your views here.
def blog(request: HttpRequest):
    return render(request, "blog.html", context={"db": db})


def post(request: HttpRequest, post_id: int):
    if post_id not in db:
        return render(request, "error_page.html")
    return render(request, "post.html", context={"post": db.get(post_id, None)})


def post_data(request: HttpRequest, post_id: int):
    res = HttpResponse(content_type="application/json")
    res.status_code = 200
    res.content = json.dumps(db.get(post_id, None))
    print(res.content)
    return res


def bookinfo(request: HttpRequest):
    """
    교육용 크롤링 페이지입니다.
    """
    url = "https://paullab.co.kr/bookservice/"
    response = requests.get(url)
    html = response.text
    soup = BeautifulSoup(html, "html.parser")
    result = [f"<p>{i.text}</p>" for i in soup.select(".book_name")]
    return HttpResponse(result)
