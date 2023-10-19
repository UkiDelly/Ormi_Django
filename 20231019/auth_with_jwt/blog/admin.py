from django.contrib import admin

from blog.models import Post, Comment, Tag


# Register your models here.
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ["pk", "title", "created_at", "creator"]


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ["pk", "content", "created_at"]


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ["pk", "name"]
