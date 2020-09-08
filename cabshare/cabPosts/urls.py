from django.urls import path

from .views import get_posts, get_search_results, get_my_posts, delete_my_post

app_name = "cabPosts"
urlpatterns = [
    path("posts/", view=get_posts, name="posts"),
    path("search/", view=get_search_results, name="search_results"),
    path("my_posts/", view=get_my_posts, name="my_posts_results"),
    path("delete_my_post/<key>", view=delete_my_post, name="delete_my_post"),
]
