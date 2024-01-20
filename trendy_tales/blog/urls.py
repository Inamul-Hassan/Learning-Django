from django.urls import path
from . import views

urlpatterns = [
    path("", views.starting_page, name="index-page"),
    path("posts", views.posts, name="all-posts"),
    path("posts/<slug:slug>", views.single_post, name="single-post")
]
