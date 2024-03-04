from django.urls import path
from . import views

urlpatterns = [
    # path("", views.review),
    # path("thank-you", views.thank_you)
    path("thank-you", views.ThankYouView.as_view()),
    path("", views.ReviewView.as_view()),
    path("reviews", views.ReviewsListView.as_view()),
    path("reviews/<int:id>", views.SingleReviewView.as_view()),
]