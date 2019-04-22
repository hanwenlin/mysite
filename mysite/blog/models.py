from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

class BlogArticle(models.Model):
    author = models.ForeignKey(User,related_name='blog_posts')
    title = models.CharField(max_length=50)
    body = models.TextField()
    publish = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-publish',)

    def __str__(self):
        return self.title


