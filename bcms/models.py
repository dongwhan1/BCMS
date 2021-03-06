from django.db import models
from django.utils import timezone
from django.conf import settings
from .choices import *
# Create your models here.
class Post(models.Model):
    author = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)
    like_user_set = models.ManyToManyField(settings.AUTH_USER_MODEL,
                                           blank=True,
                                           related_name='like_user_set',
                                           through='Like')
    @property
    def like_count(self):
        return self.like_user_set.count()

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.text

class Like(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Comment(models.Model):
    post = models.ForeignKey('bcms.Post', related_name='comments', on_delete=models.CASCADE)
    author = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.text

def publish(self):
    self.published_date = timezone.now()
    self.save()

class Map_Data(models.Model):
    author = models.CharField(max_length=200)
    loc_x = models.CharField(max_length=200)
    loc_y = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    information = models.TextField()

    def __str__(self):
        return self.title

class Suggest_Data(models.Model):
    board = models.IntegerField(choices=SUGGEST_CHOICES, default=1, blank=True)
    author = models.CharField(max_length=200)
    text = models.TextField()

    def __str__(self):
        return self.text