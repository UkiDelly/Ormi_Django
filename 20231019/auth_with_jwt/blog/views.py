from rest_framework import permissions
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from blog.models import Post, Comment
from blog.serializers import PostSerializer


# Create your views here.
class PostList(APIView):
    def get(self, request: Request):
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)


class PostCreate(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request: Request):
        request.data["creator"] = request.user.pk
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.create(serializer.validated_data)
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=400)


class PostDetail(APIView):
    def get(self, request: Request, pk: int):
        post = Post.objects.get(pk=pk)
        comments = Comment.objects.filter(post=post)
        if post is None:
            return Response({"error": "Not found"}, status=404)
        serializer = PostSerializer(post)
        return Response(serializer.data)

    def put(self, request: Request, pk: int):
        if not request.user.is_authenticated:
            return Response(status=403)

        post = Post.objects.get(pk=pk)

        if post.creator != request.user:
            return Response({"error": "수정 권한이 없습니다."}, status=403)

        request.data["creator"] = request.user.pk
        serializer = PostSerializer(post, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=400)

    def delete(self, request: Request, pk: int):
        if not request.user.is_authenticated:
            return Response(status=403)

        post = Post.objects.get(pk=pk)
        if post is None:
            return Response({"error": "Not found"}, status=404)

        if post.creator != request.user:
            return Response({"error": "수정 권한이 없습니다."}, status=403)

        post.delete()
        return Response(status=200)
