from django.urls import path
from . import views

urlpatterns = [
    path("", views.qnas, name="qna"),
    path("<int:qna_id>", views.qna),
]
