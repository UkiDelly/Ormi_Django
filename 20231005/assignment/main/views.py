from django.http import HttpRequest, HttpResponse


# Create your views here.
def index(request: HttpRequest):
    return HttpResponse("어서오세요")


def about(request: HttpRequest):
    return HttpResponse("회사 정보")


def contact(request: HttpRequest):
    return HttpResponse("오시는 길")
