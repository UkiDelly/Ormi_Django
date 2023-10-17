from django.contrib.auth.decorators import login_required
from django.urls import path

from tube.views import (
    TubeListView,
    TubeCreateView,
    TubeDetailView,
    TubeUpdateView,
    comment_new,
)

app_name = "tube"

urlpatterns = [
    path("", TubeListView.as_view(), name="tube_list"),
    path("<int:pk>/", TubeDetailView.as_view(), name="tube_detail"),
    path("create/", login_required(TubeCreateView.as_view()), name="tube_create"),
    path("update/<int:pk>/", TubeUpdateView.as_view(), name="tube_update"),
    path("delete/<int:pk>/", TubeDetailView.as_view(), name="tube_delete"),
    path("<int:pk>/comment/new/", comment_new, name="comment_new"),
]
