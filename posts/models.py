from django.db import models


# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=50)
    text = models.TextField(blank=True)
    active = models.BooleanField(default=False)
    publish_date = models.DateField(null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)