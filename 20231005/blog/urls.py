from django.urls import path
from .views import blog, post


urlpatterns = [
    path("", blog, name="blog"),
    path("<int:post_id>", post, name="post"),
]
