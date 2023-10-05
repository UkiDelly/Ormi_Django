from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("main.urls")),
    path("accounts", include("accounts.urls")),
    path("blog", include("blog.urls")),
]
