# Create your views here.
from django.db.models import Q
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)

from blog.models import Post


class PostList(ListView):
    model = Post
    ordering = "-pk"
    # template_name = 'blog/변경.html'

    def get_queryset(self):
        query_set = super().get_queryset()

        # reqeust의 GET 파라미터에서 'q'를 가져옵니다.
        q = self.request.GET.get("q")

        # 'q' 파라미터가 제공되었을 경우, 쿼리셋을 필터링한다.
        if q:
            query_set = query_set.filter(
                Q(titol__icontains=q) | Q(content__icontains=q)
            )

            return query_set


class PostDetail(DetailView):
    model = Post


class PostCreate(CreateView):
    model = Post
    fields = "__all__"
    success_url = reverse_lazy("postlist")


class PostUpdate(UpdateView):
    model = Post
    fields = "__all__"
    success_url = reverse_lazy("postlist")


class PostDelete(DeleteView):
    model = Post
    success_url = reverse_lazy(
        "postlist"
    )  # 삭제되고 처리가 다 완료되지 않았을 수 있으니 지연 필요한 reverse_lazy를 사용함.


class PostTest(DetailView):
    model = Post

    def get(self, request, **kwargs):
        return HttpResponse("PostTest get")

    def post(self, request):
        return HttpResponse("PostTest post")


postlist = PostList.as_view()  # as_view는 진입 메소드
postdetail = PostDetail.as_view()
write = PostCreate.as_view()
edit = PostUpdate.as_view()
delete = PostDelete.as_view()
test = PostTest.as_view()
