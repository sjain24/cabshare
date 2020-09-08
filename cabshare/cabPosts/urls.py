from django.urls import path

from .views import *

app_name = "cabPosts"
urlpatterns = [
    # posts/ will be later moved to home/
    path("home/", TemplateView.as_view(template_name="cabPosts/home.html"), name="main"),
    path("posts/", view=get_posts, name="posts"),
    # new page required for my_posts/
    path("my_posts/", view=get_my_posts, name="my_posts_results"),
    path("delete_my_post/<key>", view=delete_my_post, name="delete_my_post"),
    path("edit_my_post/<key>", view=edit_my_post, name="edit_my_post"),
]
