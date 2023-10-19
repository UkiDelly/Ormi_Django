from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

from assignment import settings

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", RedirectView.as_view(url="tube/"), name="root"),
    path("accounts/", include("accounts.urls")),
    path("tube/", include("tube.urls")),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
