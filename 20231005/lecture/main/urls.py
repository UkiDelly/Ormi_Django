from django.urls import path
from .views import about, contact, index


urlpatterns = [
    path("", index),
    path("about", about),
    path("contact", contact),
]
