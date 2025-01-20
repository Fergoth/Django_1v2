from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

from places.models import Place


def place_details(request, place_id):
    place_queryset = Place.objects.prefetch_related('images')
    place = get_object_or_404(place_queryset, id=place_id)
    serialized_place = {
        'title': place.title,
        'imgs': [image.image.url for image in place.images.all()],
        'short_description': place.short_description,
        'long_description': place.long_description,
        'coordinates': {
            'lat': place.latitude,
            'lon': place.longitude
        }
    }
    return JsonResponse(
        serialized_place,
        json_dumps_params={
            'ensure_ascii': False,
            'indent': 4
        }
    )


def show_main(request):

    places = Place.objects.all()
    places = {
        "type": "FeatureCollection",
        "features": [
            {
                "type": "Feature",
                "geometry": {
                    "type": "Point",
                    "coordinates": [place.longitude, place.latitude]
                },
                "properties":
                {
                    "title": place.title,
                    "placeId": place.id,
                    "detailsUrl": reverse(place_details, args=[place.id])
                }
            }
            for place in places
        ]
    }
    return render(request, 'index.html', context={'places': places})
