from django.core.management.base import BaseCommand, CommandError
import requests
from io import BytesIO
from django.core import files
from places.models import Place, Image
import os
from django.core.exceptions import ObjectDoesNotExist

class Command(BaseCommand):
    help = 'Load files'

    def add_arguments(self, parser):
        parser.add_argument('url', type=str, help='Json url')

    def handle(self, *args, **kwargs):
        url = kwargs['url']

        response = requests.get(url)
        response.raise_for_status()

        response = response.json()

        title = response['title']
        imgs_url = response['imgs']
        description_short = response['description_short']
        description_long = response['description_long']
        coordinates = response['coordinates']

        place = Place.objects.get_or_create(
            title=title,
            description_short=description_short,
            description_long=description_long,
            lat=coordinates['lat'],
            lon=coordinates['lng']
        )

        for count, img_url in enumerate(imgs_url, start=1):
            response = requests.get(img_url)
            response.raise_for_status()

            position = (count)
            image_place = Image.objects.get_or_create(position=position, place=place)[0]

            img_byte = BytesIO(response.content)
            filename = os.path.basename(img_url)
            
            image_place.image.save(filename, files.File(img_byte), save=True)

        





