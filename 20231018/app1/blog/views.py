from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.status import HTTP_404_NOT_FOUND, HTTP_406_NOT_ACCEPTABLE
from rest_framework.views import APIView

from blog.models import Post
from blog.serializers import PostSerilazier


# Create your views here.
# class PostListView(ListView):
#     model = Post
#     template_name = 'blog/post_list.html'
#     context_object_name = "posts"


# def post_list(reqeust: HttpRequest):
#     post = [
#         {"title": "1", "content": "11"},
#         {"title": "2", "content": "22"},
#         {"title": "3", "content": "33"},
#     ]
#     return render(reqeust, "blog/post_list.html", {"posts": post})
# def post_list(reqeust: HttpRequest):
#     post = [
#         {"title": "1", "content": "11"},
#         {"title": "2", "content": "22"},
#         {"title": "3", "content": "33"},
#     ]
#     return JsonResponse(post, safe=False)


# Django Rest Framework 사용


# FBV 사용하는 방식
# @api_view(["GET"])
# def post_list(request: HttpRequest):
#     posts = [
#         {"title": "1", "content": "11"},
#         {"title": "2", "content": "22"},
#         {"title": "3", "content": "33"},
#     ]
#     serializer = posts
#     return Response(serializer)


# @api_view(["GET"])
# def post_list(request: Request, format=None):
#     posts = Post.objects.all()
#     serializer = PostSerilazier(posts, many=True)  # 다수의 QeurySet을 넘길때는 many=True
#     return Response(serializer.data, status=HTTP_200_OK)


# CBV 사용하는 방식
class PostList(APIView):
    def get(self, reqeust: Request):
        posts = Post.objects.all()
        serializer = PostSerilazier(posts, many=True)
        return Response(serializer.data)


class PostDetail(APIView):
    def get(self, reqeust: Request, pk):
        try:
            post = Post.objects.get(pk=pk)
            serializer = PostSerilazier(post)
            return Response(serializer.data)
        except Post.DoesNotExist:
            return Response({"error": "Not found"}, status=HTTP_404_NOT_FOUND)

    def put(self, request: Request, pk):
        try:
            post = Post.objects.get(pk=pk)
            request.data["creator"] = post.creator.pk
            serializer = PostSerilazier(data=request.data)
            print(serializer)
            if serializer.is_valid():
                serializer.update(post, request.data)
                return Response(serializer.data)
            else:
                return Response(serializer.errors, status=HTTP_406_NOT_ACCEPTABLE)
        except Post.DoesNotExist:
            return Response({"error": "Not found"}, status=HTTP_404_NOT_FOUND)
