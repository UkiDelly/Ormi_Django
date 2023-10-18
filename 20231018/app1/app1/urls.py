from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from app1 import settings
from blog.admin import myadminsite

urlpatterns = [
    path("admin/", myadminsite.urls),#admin.site.urls),
    path("blog/", include("blog.urls")),
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)