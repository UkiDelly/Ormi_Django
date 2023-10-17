from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)

from .forms import TubeForm, CommentForm
from .models import Tube


# Create your views here.
class TubeListView(ListView):
    model = Tube
    template_name = "tube/tube_list.html"
    context_object_name = "tubes"

    # 검색 기능을 위해 정의
    def get_queryset(self):
        query_set = super().get_queryset()

        # 키워드를 기주으로 검색
        q = self.request.GET.get("q")
        if q:
            query_set = query_set.filter()

        #  tag를 기준으로 검색
        tag = self.request.GET.get("tag")
        if tag:
            print(tag)
            query_set = query_set.filter(tags__name=tag)
        return query_set


class TubeDetailView(DetailView):
    model = Tube
    template_name = "tube/tube_detail.html"

    # context_object_name = "tube" # 원하는 이름으로 context_object_name를 설정할수 있다.

    def get_context_data(self, **kwargs):
        """
        여기서 원하는 쿼리셋이나 object를 추가한 후 템플릿으로 전달 할수 있다.
        """
        context = super().get_context_data(**kwargs)
        context["comment_form"] = CommentForm()
        return context

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        obj.view_count += 1
        obj.save()
        return obj


class TubeCreateView(LoginRequiredMixin, CreateView):
    model = Tube
    form_class = TubeForm
    template_name = "tube/tube_form.html"

    def form_valid(self, form):
        form.instance.creator = self.request.user
        return super().form_valid(form)


#
class TubeUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Tube
    form_class = TubeForm
    template_name = "tube/tube_form.html"

    def test_func(self):
        tube = self.get_object()
        return tube.creator == self.request.user


class PostDeleteView(UserPassesTestMixin, DeleteView):
    model = Tube
    success_url = reverse_lazy("tube:tube_list")

    def test_func(self):
        # UserPassesTestMixin에 있고 test_func() 메서드를 오버라이딩, True, False 값으로 접근 제한
        return self.get_object().author == self.request.user


@login_required(redirect_field_name="/accounts/login/", login_url="/accounts/login/")
def comment_new(request, pk):
    post = Tube.objects.get(pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)  # commit=False는 DB에 저장하지 않고 객체만 반환
            comment.post = post
            comment.author = request.user
            comment.save()
            return redirect("tube:tube_detail", pk)
    else:
        form = CommentForm()
    return render(
        request,
        "tube/tube_form.html",
        {"comment_form": form},
    )
