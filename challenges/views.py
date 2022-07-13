from django.shortcuts import render
from django.http import Http404, HttpResponseRedirect, HttpResponseNotFound
from django.urls import reverse
# from django.template.loader import render_to_string


months = {'january': "january data",
          'february': "february data",
          'march': "march data",
          'april': "april data",
          'may': "may data",
          'june': "june data",
          'july': "july data",
          'august': "august data",
          #   'september': "september data",
          #   'october': "october data",
          'september': None,
          'october': None,
          'november': "november data",
          'december': "december data", }


# Create your views here.


def index(request):
    months_list = list(months.keys())

    return render(request, "challenges/index.html", {
        "months": months_list
    })


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
            "month_name": month,
        })
    except KeyError as exc:
        # response_data = render_to_string("404.html")
        # return HttpResponseNotFound(response_data)
        raise Http404() from exc
