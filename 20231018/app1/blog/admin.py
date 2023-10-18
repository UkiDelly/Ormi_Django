

from django.contrib import admin
from django.contrib.admin import AdminSite
from django.utils.translation import gettext_lazy as _

from blog.models import Post, Comment, Tag


# Register your models here.
# class PostAdmin(admin.ModelAdmin):
#     list_display = ["title", "created_at"]
#
#
# class CommentAdmin(admin.ModelAdmin):
#     list_display = ["message", "created_at"]
#
#
# class TagAdmin(admin.ModelAdmin):
#     list_display = ["name"]
#
#
# admin.site.register(Post, PostAdmin)
# admin.site.register(Comment, CommentAdmin)
# admin.site.register(Tag, TagAdmin)
class MyAdminSite(AdminSite):
    # site_title = _('My Site APP Custom Admin')
    # site_header = _('My Site Administration')
    index_title = _('Dashboard Test!!')


class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'content_size', 'created_at', 'updated_at']
    
    def content_size(self, post):
        return '{}글자'.format(len(post.content))
    content_size.short_description = '글자수'


myadminsite = MyAdminSite(name='myadmin')
myadminsite.register(Post, PostAdmin)