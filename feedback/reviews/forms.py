from django import forms


class ReviewForm(forms.Form):
    username = forms.CharField(label="Your Name", max_length=100)
