from django.urls import path

from . import views

urlpatterns = [
    path("", views.ProfileView.as_view()),
    path("list", views.AllProfilesView.as_view()),
]
