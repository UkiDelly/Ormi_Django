from django.urls import path
from . import views

urlpatterns = [
    path("", views.choose, name="notice"),
    path("free", views.free_feed),
    path("free/<int:free_id>", views.free),
    path("oneone", views.oneones),
    path("oneone/<int:oneone_id>", views.oneone),
]
