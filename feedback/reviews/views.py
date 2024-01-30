from django.shortcuts import render
from django.http import HttpResponseRedirect
from . import forms
from .models import ReviewModel
# Create your views here.
from django.views import View


class ReviewView(View):

    def get(self, request):
        form = forms.ReviewForm()
        return render(request, 'reviews/index.html', {'form': form})

    def post(self, request):
        form = forms.ReviewForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            form.save()
            return HttpResponseRedirect('/thank-you')
        form = forms.ReviewForm()
        return render(request, 'reviews/index.html', {'form': form})

# def index(request):
#     if request.method == "POST":
#         form = forms.ReviewForm(request.POST)
#         if form.is_valid():
#             # review = ReviewModel(user_name=form.cleaned_data['username'],
#             #                      reviews=form.cleaned_data['reviews'],
#             #                      rating=form.cleaned_data['rating'])
#             # review.save()

#             print(form.cleaned_data)
#             form.save()
#             return HttpResponseRedirect('/thank-you')
#     else:
#         form = forms.ReviewForm()

#     return render(request, 'reviews/index.html', {'form': form})


def thank_you(request):
    return render(request, 'reviews/thank-you.html')
