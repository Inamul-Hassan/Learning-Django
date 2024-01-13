from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from typing import Dict, Any, List
from django.urls import reverse

# Create your views here.

# Try 1
# def january(request):
#     return HttpResponse("Complete Django Course")


# def febuary(request):
#     return HttpResponse('Built A Real World Project with Django & AI(RAG)')

# Try 2
# def monthly_challenges(request, month: str) -> HttpResponse:
#     match month:
#         case "january":
#             return HttpResponse("Learn Django: Zero to One")
#         case "febuary":
#             return HttpResponse("Built A Real World Project with Django & AI(RAG)")
#         case _:
#             return HttpResponseNotFound("Invalid month")

# if month == "january":
#     challenge_text = "Complete Django Course"
# elif month == "febuary":
#     challenge_text = "Built A Real World Project with Django & AI(RAG)"
# else:
#     return HttpResponseNotFound('Invalid Month')
# return challenge_text

# Try 3

challenges_text: Dict = {
    'january': "Learn Django: Zero to One",
    'febuary': "Built A Real World Project with Django & AI(RAG)",
    'march': "Refresh AI/ML Concepts and Start Taking Interviews",
    'april': "Resign PwC",
    'may': "Start At New Job"
}


def index(request: Any) -> Any:
    list_items: str = ""
    months: List = list(challenges_text.keys())

    for month in months:
        capitalized_month: str = month.capitalize()
        month_path: str = reverse("monthly-challenges", args=[month])
        list_items += f"<li><a href=\"{month_path}\">{capitalized_month}</a></li>"
    return HttpResponse(f"<ul>{list_items}</ul>")


def monthly_challenges_by_number(request: Any, month: int) -> Any:
    months: List = list(challenges_text.keys())
    if month > len(months) or month <= 0:
        return HttpResponseNotFound("Invalid Month")
    else:
        redirect_month = months[month-1]
        # reverse() -> to derive the actual path/route from name of the route
        month_path: str = reverse("monthly-challenges", args=[redirect_month])
        print(month_path)
        return HttpResponseRedirect(month_path)


def monthly_challenges(request: Any, month: str) -> Any:
    try:
        return HttpResponse(challenges_text[month])
    except:
        return HttpResponseNotFound("Invalid Month")
