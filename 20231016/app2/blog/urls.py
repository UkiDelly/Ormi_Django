from django.urls import path

from .views import PostList, PostDetail, PostCreate

urlpatterns = [
    path("", PostList.as_view(), name="postlist"),
    path("<int:pk>/", PostDetail.as_view(), name="postdetail"),
    path("create/", PostCreate.as_view(), name="postcreate"),
]
