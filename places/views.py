from django.shortcuts import render
from .models import Place, Image
import json

def index(request):
    places = Place.objects.all()

    features = []
    for place in places:
        features.append(
            {
                "type": "Feature",
                "geometry": {
                    "type": "Point",
                    "coordinates": [place.lon, place.lat],
            },
                "properties": {
                    "title": place.point_title,
                    "placeId": place.id,
                    "detailsUrl": place.id
                }
            }
        )
        
    
    places_geojson = {
        "type": "FeatureCollection",
        "features": features,
    }


    return render(request, 'index.html', {'places_geojson': places_geojson})
