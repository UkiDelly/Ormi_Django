from django.urls import path
from . import views

urlpatterns = [
    path("", views.error),
    path("login/", views.login),
    path("logout/", views.logout),
]
