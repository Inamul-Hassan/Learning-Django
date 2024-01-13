from django.urls import path
from . import views

# URLconfs
urlpatterns = [
    # path(route='january', view=views.january),
    # path(route='febuary', view=views.febuary),
    path(route="", view=views.index),
    path(route='<int:month>', view=views.monthly_challenges_by_number),
    path(route='<str:month>', view=views.monthly_challenges,
         name="monthly-challenges")

]
