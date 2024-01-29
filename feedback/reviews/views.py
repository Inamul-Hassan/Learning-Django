from django.shortcuts import render
from django.http import HttpResponseRedirect
from . import forms
# Create your views here.


def index(request):
    if request.method == "POST":
        form = forms.ReviewForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            return HttpResponseRedirect('/thank-you')
    else:
        form = forms.ReviewForm()

    return render(request, 'reviews/index.html', {'form': form})


def thank_you(request):
    return render(request, 'reviews/thank-you.html')
