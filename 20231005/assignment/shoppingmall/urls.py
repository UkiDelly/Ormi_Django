from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("main.urls")),
    path("products/", include("product.urls")),
    path("qna/", include("qna.urls")),
    path("notice/", include("notice.urls")),
]
