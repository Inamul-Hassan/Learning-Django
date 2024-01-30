from django import forms
from .models import ReviewModel


# class ReviewForm(forms.Form):
#     username = forms.CharField(label="Your Name", max_length=100)
#     reviews = forms.CharField(
#         label="Your Review", max_length=200, widget=forms.Textarea)
#     rating = forms.IntegerField(label="Your Rating", min_value=1, max_value=5)


class ReviewForm(forms.ModelForm):
    class Meta:
        model = ReviewModel
        fields = "__all__"
        labels = {
            "user_name": "Your Name",
            "reviews": "Your Review",
            "rating": "Your Rating",
        }
        error_messages = {
            "user_name": {
                "required": "Please enter your name",
                "max_length": "Please enter a shorter name",
            },
            "reviews": {
                "required": "Please enter your review",
                "max_length": "Please enter a shorter review",
            }
        }
