from django.contrib import admin
from .models import Post, Comment

admin.site.register(Post, Comment)

# Register your models here.
