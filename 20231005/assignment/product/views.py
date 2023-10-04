import json
from django.http import HttpRequest, HttpResponse
import random

# 가상의 상품 데이터를 생성할 리스트
datas = []
ranks = [x for x in range(1, 11)]
random.shuffle(ranks)
# 10개의 상품 생성
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


# Create your views here.
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
