from django.contrib import admin

from .models import Post


class PostAdmin(admin.ModelAdmin):
    list_display = [
        'id', 'title', 'created_time', 'publish_date', 'updated_time', 'active'

    ]


admin.site.register(Post, PostAdmin)
