from django.contrib import admin

from blog.models import Post, Comment, Tag


# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display = ["title", "created_at"]


class CommentAdmin(admin.ModelAdmin):
    list_display = ["message", "created_at"]


class TagAdmin(admin.ModelAdmin):
    list_display = ["name"]


admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Tag, TagAdmin)
