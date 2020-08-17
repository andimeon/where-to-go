from django.shortcuts import render, get_object_or_404
from .models import Place, Image
from django.http import HttpResponse
import json
from django.urls import reverse


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
                    "title": place.title,
                    "placeId": place.id,
                    "detailsUrl": reverse('endpoint', args=(place.id,))
                }
            }
        )
        
    places_geojson = {
        "type": "FeatureCollection",
        "features": features,
    }

    return render(request, 'index.html', {'places_geojson': places_geojson})


def endpoint(request, id):
    place = get_object_or_404(Place, id=id)

    images_url = [image.image.url for image in place.images.all()]

    place_json = {
        "title": place.title,
        "imgs": images_url,
        "short_description": place.short_description,
        "long_description": place.long_description,
        "coordinates": {
            "lat": place.lat,
            "lng": place.lon,
        }
    }

    return HttpResponse(json.dumps(place_json, indent=4, ensure_ascii=False), content_type="application/json")
