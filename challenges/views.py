from django.http import HttpResponse
# from django.shortcuts import render

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


def monthly_challenge(request, month):
    challenge_text = None
    if month in months:
        challenge_text = months[month]
    else:
        challenge_text = f"Month *{month}* is Not supported"
    return HttpResponse(challenge_text)
