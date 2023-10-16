from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView

from .models import Post


# Create your views here.
class PostList(ListView):
    model = Post
    ordering = "-pk"


class PostDetail(DetailView):
    model = Post


class PostCreate(CreateView):
    model = Post
    fields = "__all__"
    success_url = reverse_lazy("postlist")
