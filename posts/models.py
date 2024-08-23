from django.db import models


class PostLiveManager(models.Manager):

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(id = 1)
        return queryset

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=50)
    text = models.TextField(blank=True)
    active = models.BooleanField(default=False)
    publish_date = models.DateField(null=True, blank=True)
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)

    objects = models.Manager()
    live = PostLiveManager()

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    text = models.TextField()
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)
