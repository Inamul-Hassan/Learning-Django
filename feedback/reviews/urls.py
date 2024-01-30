from django.urls import path
from . import views

urlpatterns = [
    path("", views.ReviewView.as_view(), name="index"),
    path("thank-you", views.ThankYouView.as_view(), name="thank_you"),
    path("all-reviews", views.AllReviewsView.as_view(), name="all_reviews"),
    path("review/<int:id>", views.DetailedReviewView.as_view(), name="review_detail"),
]
