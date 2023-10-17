from django.contrib import admin

from .models import Comment, Tag, Tube


# Register your models here.
class TubeAdmin(admin.ModelAdmin):
    list_display = ["title", "creator"]


class CommentAdmin(admin.ModelAdmin):
    list_display = ["content", "created_at", "updated_at"]


class TagAdmin(admin.ModelAdmin):
    list_display = ["name"]


admin.site.register(Tube, TubeAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Tag, TagAdmin)
