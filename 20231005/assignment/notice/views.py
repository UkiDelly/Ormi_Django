import json
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

freeboard_data = []

# 10개의 게시물 생성
for i in range(1, 11):
    post = {
        "id": i,
        "title": f"게시물 제목 {i}",
        "content": f"게시물 {i}의 내용입니다. 이것은 가상의 게시물입니다.",
    }
    freeboard_data.append(post)


inquiry_data = []

# 10개의 1대1 문의 생성
for i in range(1, 11):
    inquiry = {
        "id": i,
        "subject": f"1대1 문의 제목 {i}",
        "message": f"1대1 문의 {i}에 대한 내용입니다. 이것은 가상의 1대1 문의입니다.",
    }
    inquiry_data.append(inquiry)


# Create your views here.
def choose(request: HttpRequest):
    return render(request, "choose.html")


def free_feed(request: HttpRequest):
    return HttpResponse(json.dumps(freeboard_data))


def free(request: HttpRequest, free_id: int):
    try:
        feed = list(filter(lambda x: x["id"] == free_id, freeboard_data))[0]
        return HttpResponse(json.dumps(feed))
    except IndexError:
        res = HttpResponse(json.dumps({"error": "not found"}))
        res.status_code = 404
        return res


def oneones(request: HttpRequest):
    return HttpResponse(json.dumps(inquiry_data))


def oneone(request: HttpRequest, oneone_id: int):
    try:
        inquiry = list(filter(lambda x: x["id"] == oneone_id, inquiry_data))[0]
        return HttpResponse(json.dumps(inquiry))
    except IndexError:
        res = HttpResponse(json.dumps({"error": "not found"}))
        res.status_code = 404
        return res


"""
|앱 이름: main|views 함수 이름|html 파일이름|비고|
|''|indes|index||
|'/about'|about|about||
|'/contact|countact|contact||

|앱 이름: product|views 함수 이름|html 파일이름|비고|
|'/products'|products|None|json 데이터|
|'/product/<int:product_id>'|product|None|json 데이터|

|앱 이름: qna|views 함수 이름|None|비고|
|'/qna'|qnas|None|json 데이터|
|'/qna/<int:qna_id>|qna|None|json 데이터|
|
|앱 이릅: notice|views 함수 이름|html 파일이름|비고|
|'/notice'|choose|choose.html||
|'/notice/free|free_feed|None|json 데이터|
|'/notice/free/<int:free_id>'|free|None|json 데이터|
|'/notice/oneone'|oneones|None|json 데이터|
|'/notice/oneone/<int:oneone_id>'|oneone|None|json 데이터|
"""
