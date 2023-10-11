from django.urls import path

from . import views


urlpatterns = [
    path("", views.blog, name="blog"),
    path("upload_image/", views.upload_image),
    path("<int:post_id>/", views.post, name="blog"),
]
