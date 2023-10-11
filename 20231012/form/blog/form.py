from django import forms

from .models import Post


class LicatForm(forms.Form):
    title = forms.CharField(max_length=20)
    contents = forms.CharField()


class PostForm(forms.ModelForm):
    class Meta:
        # 이 Form에서 사용하는 모델
        model = Post
        # Post의 어떤 필드와 매칭할 것인지 결정
        # fields = ["title", "contents", "main_image"]
        fields = "__all__"
