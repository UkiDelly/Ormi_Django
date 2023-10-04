import json
from django.http import HttpRequest, HttpResponse

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
