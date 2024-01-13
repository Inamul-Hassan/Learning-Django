from django.urls import path
from . import views

# URLconfs
urlpatterns = [
    path(route='january', view=views.index)
]
