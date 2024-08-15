from django.contrib import admin

from .models import Post, Comment


class PostAdmin(admin.ModelAdmin):
    list_display = [
        'id', 'title', 'created_time', 'publish_date', 'updated_time', 'active'
    ]


class CommentAdmin(admin.ModelAdmin):
    list_display = [
        'id', 'post', 'created_time', 'updated_time'
    ]


admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
