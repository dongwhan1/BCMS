from django.contrib import admin
from .models import Post, Comment, Post2, Comment2
# Register your models here.
admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Post2)
admin.site.register(Comment2)