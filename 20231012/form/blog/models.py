from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=100)
    contents = models.TextField()
    main_image = models.ImageField(upload_to="blog/%Y/%m/%d/", blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def to_json(self):
        return {
            "id": self.pk,
            "title": self.title,
            "contents": self.contents,
            "main_image": self.main_image.url,
            "created_at": self.created_at,
            "updated_at": self.updated_at,
        }

    def __str__(self):
        return f"{self.title}"
