from django.shortcuts import render
from django.views import View
from django.http import HttpResponseRedirect
# from .forms import ReviewForm
# Create your views here.
from .models import ReviewModel
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView


class ProfileView(CreateView):
    model = ReviewModel
    template_name = "profiles/create_profile.html"
    success_url = "/profiles/"
    fields = "__all__"


class AllProfilesView(ListView):
    model = ReviewModel
    template_name = "profiles/user-profiles.html"
    context_object_name = "profiles"


# def store_data(file):
    # with open("temp/image.jpg", "wb+") as destination:
    #     for chunk in file.chunks():
    #         destination.write(chunk)


# class CreateProfileView(View):
#     def get(self, request):
#         form = ReviewForm()
#         return render(request, "profiles/create_profile.html", {"form": form})

#     def post(self, request):
#         submitted_form = ReviewForm(request.POST, request.FILES)

#         if submitted_form.is_valid:
#             submission = ReviewModel(image=request.FILES["user_image"])
#             submission.save()
#             return HttpResponseRedirect("/profiles")
#         return render(request, "profiles/create_profile.html", {"form": submitted_form})
