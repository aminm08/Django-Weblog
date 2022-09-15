from django.contrib import admin

from .models import BlogPost, Comment

@admin.register(BlogPost)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'datetime_modified')

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('author', 'active', 'datetime_modified')


