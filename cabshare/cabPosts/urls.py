from django.urls import path

from .views import get_posts

app_name = "cabPosts"
urlpatterns = [
    path("posts/", view=get_posts, name="posts"),
]
