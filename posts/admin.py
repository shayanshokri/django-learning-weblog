from django.contrib import admin

from .models import Post, Comment


class CommentAdminInline(admin.TabularInline):
    model = Comment
    fields = ['text']
    extra = 0


class PostAdmin(admin.ModelAdmin):
    list_display = [
        'id', 'title', 'created_time', 'publish_date', 'updated_time', 'active'
    ]
    inlines = [CommentAdminInline]


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = [
        'id', 'post', 'created_time', 'updated_time'
    ]


admin.site.register(Post, PostAdmin)
# admin.site.register(Comment, CommentAdmin)
