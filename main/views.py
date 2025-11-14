import random
from datetime import date
from .models import Artist
from django.http import JsonResponse
from django.shortcuts import render

from django.db import transaction
from django.utils.timezone import now
from datetime import datetime, timedelta

# Create your views here.
def get_birthdays(request):

    today = date.today()

    matches = Artist.objects.filter(
        date_of_birth__month=today.month,
        date_of_birth__day=today.day
    )

    birthdays = [
        {
            "name": artist.name,
            "birthday": artist.date_of_birth.strftime("%Y"),
            "age": today.year - artist.date_of_birth.year
        }
        for artist in matches
    ]

    return JsonResponse(birthdays, safe=False)