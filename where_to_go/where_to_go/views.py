from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, JsonResponse
from places.models import Place


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
                    "detailsUrl": ""
                }
            }
            for place in places
        ]
    }
    return render(request, 'index.html', context={'places': places})


def place_details(request, place_id):
    place_queryset = Place.objects.prefetch_related('images')
    place = get_object_or_404(place_queryset, id=place_id)
    serialized_place = {
        'title': place.title,
        'imgs': [image.image.url for image in place.images.all()],
        'description_short': place.description_short,
        'description_long': place.description_long,
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
