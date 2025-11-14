import random
from datetime import date
from .models import Artist
from django.http import JsonResponse
from django.shortcuts import render

from django.db import transaction
from django.utils.timezone import now
from datetime import datetime, timedelta
from django.views.decorators.csrf import csrf_exempt

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


# views.py

ARTISTS_DATA = [
    {"name": "Kabza De Small","birth_date": "1992-11-27","zodiac": "Sagittarius"},
    {"name": "DJ Maphorisa","birth_date": "1987-11-15","zodiac": "Scorpio"},
    {"name": "Tyla","birth_date": "2002-01-30","zodiac": "Aquarius"},
    {"name": "Kelvin Momo","birth_date": "1994-03-20","zodiac": "Pisces"},
    {"name": "Black Coffee","birth_date": "1976-03-11","zodiac": "Pisces"},
    {"name": "Master KG","birth_date": "1996-01-31","zodiac": "Aquarius"},
    {"name": "Tyler ICU","birth_date": "1997-06-12","zodiac": "Gemini"},
    {"name": "Nasty C","birth_date": "1997-02-11","zodiac": "Aquarius"},
    {"name": "Zee Nxumalo","birth_date": "1999-09-05","zodiac": "Virgo"},
    {"name": "Cassper Nyovest","birth_date": "1990-12-16","zodiac": "Sagittarius"},
    {"name": "MaWhoo","birth_date": "1995-07-22","zodiac": "Cancer"},
    {"name": "A-Reece","birth_date": "1997-03-27","zodiac": "Aries"},
    {"name": "Sjava","birth_date": "1984-12-02","zodiac": "Sagittarius"},
    {"name": "Big Zulu","birth_date": "1986-04-07","zodiac": "Aries"},
    {"name": "K.O","birth_date": "1981-10-13","zodiac": "Libra"},
    {"name": "Emtee","birth_date": "1992-09-17","zodiac": "Virgo"},
    {"name": "Blxckie","birth_date": "1999-05-24","zodiac": "Gemini"},
    {"name": "Nkosazana Daughter","birth_date": "2000-10-06","zodiac": "Libra"},
    {"name": "Scotts Maphuma","birth_date": "1996-08-14","zodiac": "Leo"},
    {"name": "Usimamane","birth_date": "1998-11-03","zodiac": "Scorpio"},
    {"name": "Elaine","birth_date": "1998-04-02","zodiac": "Aries"},
    {"name": "Vigro Deep","birth_date": "2001-09-12","zodiac": "Virgo"},
    {"name": "Lira","birth_date": "1979-03-14","zodiac": "Pisces"},
    {"name": "Thandiswa Mazwai","birth_date": "1976-03-31","zodiac": "Aries"},
    {"name": "Shane Eagle","birth_date": "1996-09-07","zodiac": "Virgo"},
    {"name": "King Monada","birth_date": "1993-05-25","zodiac": "Gemini"},
    {"name": "Makhadzi","birth_date": "1996-06-30","zodiac": "Cancer"},
    {"name": "Uncle Waffles","birth_date": "2000-03-30","zodiac": "Aries"},
    {"name": "Naledi Aphiwe","birth_date": "2006-02-18","zodiac": "Aquarius"},
    {"name": "Musa Keys","birth_date": "1997-11-22","zodiac": "Scorpio"},
    {"name": "Manana","birth_date": "1995-08-09","zodiac": "Leo"},
    {"name": "Dj Fresh","birth_date": "1971-02-28","zodiac": "Pisces"},
    {"name": "Kwesta","birth_date": "1988-08-11","zodiac": "Leo"},
    {"name": "Zakwe","birth_date": "1984-06-05","zodiac": "Gemini"},
    {"name": "Ginger Trill","birth_date": "1989-10-19","zodiac": "Libra"},
    {"name": "Stogie T","birth_date": "1981-12-16","zodiac": "Sagittarius"},
    {"name": "Judith Sephuma","birth_date": "1974-05-28","zodiac": "Gemini"},
    {"name": "Lloyiso","birth_date": "1998-11-01","zodiac": "Scorpio"},
    {"name": "Nathi","birth_date": "1984-12-23","zodiac": "Capricorn"},
    {"name": "Jezzel Brothers","birth_date": "1990-07-15","zodiac": "Cancer"},
    {"name": "Vusi Nova","birth_date": "1984-09-25","zodiac": "Libra"},
    {"name": "Niapearlza","birth_date": "1997-04-17","zodiac": "Aries"},
    {"name": "Sam Deep","birth_date": "1995-10-30","zodiac": "Scorpio"},
    {"name": "DBN Gogo","birth_date": "1993-05-29","zodiac": "Gemini"},
    {"name": "Euphonik","birth_date": "1979-12-08","zodiac": "Sagittarius"},
    {"name": "Lucky Dube","birth_date": "1964-08-03","zodiac": "Leo"},
    {"name": "Die Antwoord","birth_date": "1974-09-26","zodiac": "Libra"},
    {"name": "Kamo Mphela","birth_date": "1999-11-29","zodiac": "Sagittarius"},
    {"name": "Major League DJz","birth_date": "1991-01-07","zodiac": "Capricorn"},
    {"name": "Maglera Doe Boy","birth_date": "1995-03-18","zodiac": "Pisces"},
    {"name": "Makhanj","birth_date": "1998-06-22","zodiac": "Cancer"},
    {"name": "Rouge","birth_date": "1992-09-13","zodiac": "Virgo"},
    {"name": "Msaki","birth_date": "1988-11-25","zodiac": "Sagittarius"},
    {"name": "Yvonne Chaka Chaka","birth_date": "1965-03-18","zodiac": "Pisces"},
    {"name": "TxC","birth_date": "1996-09-04","zodiac": "Virgo"},
    {"name": "Zakes Bantwini","birth_date": "1980-05-26","zodiac": "Gemini"},
    {"name": "Busiswa","birth_date": "1988-11-08","zodiac": "Scorpio"},
    {"name": "Sfarzo Rtee","birth_date": "1997-12-14","zodiac": "Sagittarius"},
    {"name": "Oscar Mbo","birth_date": "1990-04-07","zodiac": "Aries"},
    {"name": "MDU aka TRP","birth_date": "1994-08-19","zodiac": "Leo"},
    {"name": "Saudi","birth_date": "1993-02-27","zodiac": "Pisces"},
    {"name": "Tony Dayimane","birth_date": "1999-07-31","zodiac": "Leo"},
    {"name": "Ami Faku","birth_date": "1993-05-28","zodiac": "Gemini"},
    {"name": "Priddy Ugly","birth_date": "1992-04-02","zodiac": "Aries"},
    {"name": "YoungstaCPT","birth_date": "1991-12-22","zodiac": "Capricorn"},
    {"name": "Khuli Chana","birth_date": "1982-08-27","zodiac": "Virgo"},
    {"name": "Reason","birth_date": "1984-03-10","zodiac": "Pisces"},
    {"name": "L-Tido","birth_date": "1982-03-30","zodiac": "Aries"},
    {"name": "iFani","birth_date": "1985-11-20","zodiac": "Scorpio"},
    {"name": "Blacklez","birth_date": "1988-07-05","zodiac": "Cancer"},
    {"name": "Proverb","birth_date": "1981-06-08","zodiac": "Gemini"},
    {"name": "Crowned Yung","birth_date": "2000-09-11","zodiac": "Virgo"},
    {"name": "Blue Pappi","birth_date": "1997-01-15","zodiac": "Capricorn"},
    {"name": "Kane Keid","birth_date": "1996-10-03","zodiac": "Libra"},
    {"name": "Brother Kupa","birth_date": "1994-12-07","zodiac": "Sagittarius"},
    {"name": "Lucas Raps","birth_date": "2000-05-19","zodiac": "Taurus"},
    {"name": "Mfana Touchline","birth_date": "1998-08-27","zodiac": "Virgo"},
    {"name": "Focalistic","birth_date": "1996-05-26","zodiac": "Gemini"},
    {"name": "Sho Madjozi","birth_date": "1992-05-09","zodiac": "Taurus"},
    {"name": "Nadia Nakai","birth_date": "1990-05-18","zodiac": "Taurus"},
    {"name": "KindlyNxsh","birth_date": "2001-03-14","zodiac": "Pisces"},
    {"name": "Da L.E.S","birth_date": "1985-07-26","zodiac": "Leo"},
    {"name": "Kid X","birth_date": "1987-04-12","zodiac": "Aries"},
    {"name": "Maggz","birth_date": "1983-09-15","zodiac": "Virgo"},
    {"name": "25K","birth_date": "1997-06-30","zodiac": "Cancer"},
    {"name": "Loatinover Pounds","birth_date": "1999-11-08","zodiac": "Scorpio"},
    {"name": "Sizwe Alakine","birth_date": "1988-02-20","zodiac": "Pisces"},
    {"name": "Flame","birth_date": "1989-09-17","zodiac": "Virgo"},
    {"name": "Audiomarc","birth_date": "1995-04-05","zodiac": "Aries"},
    {"name": "IMP THA DON","birth_date": "1996-12-11","zodiac": "Sagittarius"},
    {"name": "Buzzi Lee","birth_date": "1998-07-23","zodiac": "Leo"},
    {"name": "Wordz","birth_date": "1997-10-29","zodiac": "Scorpio"},
    {"name": "Thato Saul","birth_date": "1996-03-04","zodiac": "Pisces"},
    {"name": "Marcus Harvey","birth_date": "1994-11-16","zodiac": "Scorpio"},
    {"name": "Costa Titch","birth_date": "1995-09-26","zodiac": "Libra"},
    {"name": "Flvme","birth_date": "1996-02-03","zodiac": "Aquarius"},
    {"name": "MashBeatz","birth_date": "1994-08-18","zodiac": "Leo"}
]


@csrf_exempt
def import_artists(request):
    """
    Creates/updates all artists in the dictionary.
    No file IO. Eliminates duplicates automatically.
    """
    created, updated = [], []

    for entry in ARTISTS_DATA:
        name = entry["name"]
        birth = entry["birth_date"]
        zodiac = entry["zodiac"]

        artist, is_created = Artist.objects.get_or_create(name=name)

        artist.date_of_birth = birth
        artist.description = f"Zodiac: {zodiac}"
        artist.save()

        if is_created:
            created.append(name)
        else:
            updated.append(name)

    return JsonResponse({
        "total_artists": len(ARTISTS_DATA),
        "created": created,
        "updated": updated,
    })
