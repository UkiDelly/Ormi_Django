from django import forms

from tube.models import Tube, Comment, Tag


class TubeForm(forms.ModelForm):
    class Meta:
        model = Tube
        fields = ["title", "content", "thumbnail", "video", "tags"]


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["content"]


class TagForm(forms.Form):
    class Meta:
        model = Tag
        fields = ["name"]
