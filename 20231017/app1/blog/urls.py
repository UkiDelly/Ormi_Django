from django.urls import path

from blog.views import PostDetail, PostCreate, PostUpdate, PostDelete, posts, tags

urlpatterns = [
    path("", posts, name="postlist"),
    path("<int:pk>/", PostDetail.as_view(), name="postdetail"),
    path("create/", PostCreate.as_view(), name="postcreate"),
    path("update/", PostUpdate.as_view(), name="postupdate"),
    path("delete/", PostDelete.as_view(), name="postdelete"),
    path("<str:tag>", tags, name="tag"),
]
