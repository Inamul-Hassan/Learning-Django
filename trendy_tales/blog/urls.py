from django.urls import path
from . import views
urlpatterns = [
    path("", views.starting_page, "index-page"),
    path("posts", views.posts, "all-posts"),
    path("posts/<slug:slug>", views.single_post, "post")
]
