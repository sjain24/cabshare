from django.urls import path

from .views import *

app_name = "cabPosts"
urlpatterns = [
    path("posts/", view=get_posts, name="posts"),
    path("my_posts/", view=get_my_posts, name="my_posts_results"),
    path("delete_my_post/<key>", view=delete_my_post, name="delete_my_post"),
    path("edit_my_post/<key>", view=edit_my_post, name="edit_my_post"),
]
