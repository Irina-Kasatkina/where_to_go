from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, JsonResponse

from .models import Place


def index(request):
    places = Place.objects.all()

    context = {'places': [serialize_place(place) for place in places]}
    return render(request, 'index.html', context)


def serialize_place(place):
    return {
        'id': place.id,
        'title': place.title,
        'longitude': str(place.longitude),
        'latitude': str(place.latitude)
    }


def place_details(request, place_id):
    place = get_object_or_404(Place, pk=place_id)

    images = [image.image.url for image in place.images.all()]
    json_payload = {
        'title': place.title, 
        'imgs': images,
        'description_short': place.short_description,
        'description_long': place.long_description,
        'coordinates': {
            'lng': place.longitude,
            'lat': place.latitude
        }
    }
    json_dumps_params = {'ensure_ascii': False, 'indent': 4}
    response = JsonResponse(json_payload, json_dumps_params=json_dumps_params)
    return HttpResponse(response, content_type='application/json')
