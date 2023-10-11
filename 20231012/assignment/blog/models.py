from django import forms
from django.db import models


# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return f"{self.title}"


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = "__all__"
