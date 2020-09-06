from django.urls import path

from .views import get_posts, get_search_results

app_name = "cabPosts"
urlpatterns = [
    path("posts/", view=get_posts, name="posts"),
    path("search/", view=get_search_results, name="search_results"),
]
