from django.shortcuts import render
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
