from django.urls import path

from .views import get_posts

app_name = "cabPosts"
urlpatterns = [
    path("~post/", view=get_posts, name="posts"),
    # path("~update/", view=user_update_view, name="update"),
    # path("<str:username>/", view=user_detail_view, name="detail"),
]
