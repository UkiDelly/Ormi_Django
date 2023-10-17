from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Tube(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    thumbnail = models.ImageField(
        upload_to="tube/images/%Y/%m/%d/", blank=True, null=True
    )
    video = models.FileField(upload_to="tube/files/%Y/%m/%d/", blank=True, null=True)
    view_count = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # User를 FK로 연결
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    tags = models.ManyToManyField("Tag", blank=True)

    def __str__(self) -> str:
        return f"{self.title}"

    def get_absolute_url(self):
        return f"/tube/{self.pk}"


class Comment(models.Model):
    # related_name은 Post에서 Comment를 부를 때 사용할 이름
    # ForeignKey는 1:N 관계를 만들어줍니다. 단, N에서 정의합니다.
    tube_id = models.ForeignKey(Tube, on_delete=models.CASCADE, related_name="comments")
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    creator = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.content}"


class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return f"{self.name}"
