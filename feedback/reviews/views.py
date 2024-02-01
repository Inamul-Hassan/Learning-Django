from typing import Any
from django.shortcuts import render
from django.http import HttpResponseRedirect
from . import forms
from .models import ReviewModel
# Create your views here.
from django.views import View
from django.views.generic.base import TemplateView


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


class ThankYouView(TemplateView):
    template_name = 'reviews/thank-you.html'


class AllReviewsView(TemplateView):
    template_name = 'reviews/all-reviews.html'

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['reviews'] = ReviewModel.objects.all()
        return context


class DetailedReviewView(TemplateView):
    template_name = 'reviews/review_detail.html'

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['review'] = ReviewModel.objects.get(id=self.kwargs['id'])
        fav_id = self.request.session.get(
            "favorite_review")
        context['is_favorite'] = fav_id == str(self.kwargs['id'])
        return context


class FavoriteView(View):
    def post(self, request):
        review_id = request.POST["id"]
        request.session["favorite_review"] = review_id
        return HttpResponseRedirect(f"/review/{review_id}")


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


# def thank_you(request):
#     return render(request, 'reviews/thank-you.html')
