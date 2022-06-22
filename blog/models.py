from django.contrib.auth.models import User
from django.utils import timezone
from django.db import models



class Post(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    slug = models.SlugField(max_length=255)

    def __str__(self):
        return self.title

