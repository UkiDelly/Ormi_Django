## shoppingmall

### urls.py

```python
urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("main.urls")),
    path("products/", include("product.urls")),
    path("qna/", include("qna.urls")),
    path("notice/", include("notice.urls")),
]
```

## main

### urls.py

```python
urlpatterns = [
    path("", views.index),
    path("about", views.about),
    path("contact", views.contact),
]
```

### views

```python
def index(request: HttpRequest):
    return HttpResponse("어서오세요")


def about(request: HttpRequest):
    return HttpResponse("회사 정보")


def contact(request: HttpRequest):
    return HttpResponse("오시는 길")
```

## product

### urls.py

```python
urlpatterns = [
    path("", views.products, name="products"),
    path("<int:product_id>", views.product),
]
```

### views

```python

datas = []
ranks = [x for x in range(1, 11)]
random.shuffle(ranks)

for i in range(1, 11):
    data = {
        "id": i,
        "name": f"상품 {i}",
        "description": f"이것은 상품 {i}의 설명입니다.",
        "price": round(random.uniform(10, 1000), 2),
        "stock": random.randint(0, 100),
        "rank": ranks[i - 1],
    }
    datas.append(data)

def products(request: HttpRequest):
    product_data = sorted(datas, key=lambda x: x["rank"])
    return HttpResponse(json.dumps(product_data))


def product(request: HttpRequest, product_id: int):
    try:
        product_data = list(filter(lambda x: x["id"] == product_id, datas))[0]
        return HttpResponse(json.dumps(product_data))
    except IndexError:
        res = HttpResponse(json.dumps({"error": "not found"}))
        res.status_code = 404
        return res
```

## qna

### urls.py

```python
urlpatterns = [
    path("", views.qnas, name="qna"),
    path("<int:qna_id>", views.qna),
]

```

### views

```python
# 가상의 Q&A 데이터를 생성할 리스트
qna_datas = []

# 10개의 묻고 응답 생성
for i in range(1, 11):
    qna_data = {
        "id": i,
        "question": f"질문 {i}",
        "answer": f"질문 {i}에 대한 답변입니다.",
    }
    qna_datas.append(qna_data)


# Create your views here.
def qnas(request: HttpRequest):
    return HttpResponse(json.dumps(qna_datas))


def qna(request: HttpRequest, qna_id: int):
    try:
        qna_data = list(filter(lambda x: x["id"] == qna_id, qna_datas))[0]
        return HttpResponse(json.dumps(qna_data))

    except IndexError:
        res = HttpResponse(json.dumps({"error": "not found"}))
        res.status_code = 404
        return res
```

## notice

### urls.py

```python
urlpatterns = [
    path("", views.choose, name="notice"),
    path("free", views.free_feed),
    path("free/<int:free_id>", views.free),
    path("oneone", views.oneones),
    path("oneone/<int:oneone_id>", views.oneone),
]
```

### views

```python
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
```

| 앱 이름: main | views 함수 이름 | html 파일이름 | 비고 |
| ------------- | --------------- | ------------- | ---- |
| ''            | indes           | index         |      |
| '/about'      | about           | about         |      |
| '/contact     | countact        | contact       |      |

---

| 앱 이름: product            | views 함수 이름 | html 파일이름 | 비고        |
| --------------------------- | --------------- | ------------- | ----------- |
| '/products'                 | products        | None          | json 데이터 |
| '/product/<int:product_id>' | product         | None          | json 데이터 |

---

| 앱 이름: qna       | views 함수 이름 | None | 비고        |
| ------------------ | --------------- | ---- | ----------- |
| '/qna'             | qnas            | None | json 데이터 |
| '/qna/<int:qna_id> | qna             | None | json 데이터 |

---

| 앱 이릅: notice                  | views 함수 이름 | html 파일이름 | 비고        |
| -------------------------------- | --------------- | ------------- | ----------- |
| '/notice'                        | choose          | choose.html   |             |
| '/notice/free                    | free_feed       | None          | json 데이터 |
| '/notice/free/<int:free_id>'     | free            | None          | json 데이터 |
| '/notice/oneone'                 | oneones         | None          | json 데이터 |
| '/notice/oneone/<int:oneone_id>' | oneone          | None          | json 데이터 |

---
