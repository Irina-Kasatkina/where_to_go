from django.shortcuts import render

from .models import Place


def index(request):
    places = Place.objects.all()

    context = {
        'places': [serialize_place(place) for place in places]
    }  
    return render(request, 'index.html', context)

def serialize_place(place):
    return {
        'id': place.id,
        'title': place.title,
        'longitude': str(place.longitude),
        'latitude': str(place.latitude)
    }