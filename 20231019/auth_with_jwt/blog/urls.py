from django.urls import path

from blog.views import PostList, PostDetail, PostCreate

app_name = "blog"
urlpatterns = [
    path("", PostList.as_view(), name="post_list"),
    path("create/", PostCreate.as_view(), name="post_create"),
    path("<int:pk>/", PostDetail.as_view(), name="post_detail"),
]
