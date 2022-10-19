from django.shortcuts import get_object_or_404, render
from django.http import JsonResponse

from .models import Place


def index(request):
    places = Place.objects.all()

    features = []
    for place in places:
        feature = {
            'type': 'Feature',
            'geometry': {
                'type': 'Point',
                'coordinates': [place.longitude, place.latitude]
            },
            'properties': {
                'title': place.title,
                'placeId': place.id,
                'detailsUrl': f'places/{place.id}'
            }
        }
        features.append(feature)

    places_geojson = {
        'type': 'FeatureCollection',
        'features': features,
    }
    context = {'places_geojson': places_geojson}
    return render(request, 'index.html', context)


def place_details(request, place_id):
    place = get_object_or_404(Place, pk=place_id)

    response = {
        'title': place.title, 
        'imgs': [image.image.url for image in place.images.all()],
        'description_short': place.short_description,
        'description_long': place.long_description,
        'coordinates': {
            'lng': place.longitude,
            'lat': place.latitude
        }
    }
    return JsonResponse(response)
