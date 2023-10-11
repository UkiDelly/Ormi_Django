from django.http import HttpRequest, JsonResponse

from img_server.settings import MEDIA_URL

from .models import Post


# Create your views here.
def blog(request: HttpRequest):
    if request.method == "POST":
        title, contents = request.POST["title"], request.POST["contents"]
        file = request.FILES["main_image"]
        post = Post.objects.create(title=title, contents=contents, main_image=file)
        return JsonResponse(
            {
                "title": post.title,
                "contents": post.contents,
                "url": post.main_image.url,
            }
        )
    else:
        posts = Post.objects.all()
        return JsonResponse({"posts": posts.values()})


def upload_image(request: HttpRequest):
    if request.method == "POST":
        file = request.FILES["main_image"]

        return JsonResponse({"url": MEDIA_URL + file.name})


def post(request: HttpRequest, post_id: int):
    post = Post.objects.get(id=post_id)
    return JsonResponse({"title": post.title, "contents": post.contents})
