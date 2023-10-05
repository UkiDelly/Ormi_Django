from django.urls import path
from .views import blog, post, post_data


urlpatterns = [
    path("", blog, name="blog"),
    path("<int:post_id>", post, name="post"),
    path("info/<int:post_id>", post_data),
]
