from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound
from django.urls import reverse
from django.template.loader import render_to_string


months = {'january': "january data",
          'february': "february data",
          'march': "march data",
          'april': "april data",
          'may': "may data",
          'june': "june data",
          'july': "july data",
          'august': "august data",
          'september': "september data",
          'october': "october data",
          'november': "november data",
          'december': "december data", }


# Create your views here.


def index(request):
    list_items = ""
    months_list = list(months.keys())

    for month in months_list:
        capitalized_month = month.capitalize()
        month_path = reverse("month-challenge", args=[month])
        list_items += f"<li><a href=\"{month_path}\">{capitalized_month}</a></li>"

    response_data = f"<h1><ul>{list_items}</ul></h1>"

    return HttpResponse(response_data)


def monthly_challenge_by_number(request, month):
    months_list = list(months.keys())

    if month < 1 or month > len(months_list):
        return HttpResponseNotFound(f"<h2>Month *{month}* is Not supported</h2>")

    redirect_month = months_list[int(month) - 1]
    redirect_path = reverse("month-challenge", args=[redirect_month])
    return HttpResponseRedirect(redirect_path)


def monthly_challenge(request, month):
    try:
        # if month in months:
        challenge_text = months[month]
        return render(request, "challenges/challenge.html", {
            "text": challenge_text,
            "item": month.capitalize(),
        })
    except KeyError:
        return HttpResponseNotFound(f"<h2>Month *{month}* is Not supported</h2>")
