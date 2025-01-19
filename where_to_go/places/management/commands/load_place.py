from django.core.management.base import BaseCommand
import requests
from places.models import Place, PlaceImage
from django.core.files.base import ContentFile
import os
from urllib.parse import urlparse


def save_image(place, url):
    filepath = urlparse(url).path
    filename = os.path.basename(filepath)
    response = requests.get(url)
    imagefile = ContentFile(response.content)
    obj = PlaceImage.objects.create(
        place=place
    )
    obj.image.save(filename, imagefile, save=True)


class Command(BaseCommand):
    help = 'Загрузка мест'

    def add_arguments(self, parser):
        parser.add_argument('url', help='Url до json файла')

    def handle(self, *args, **options):
        url = options['url']
        r = requests.get(url)
        js = r.json()
        title = js['title']
        image_urls = js['imgs']
        description_short = js['description_short']
        description_long = js['description_long']
        lng = js['coordinates']['lng']
        lat = js['coordinates']['lat']
        place, created = Place.objects.get_or_create(
            title=title,
            description_long=description_long,
            description_short=description_short,
            longitude=lng,
            latitude=lat
        )
        if created:
            for image_url in image_urls:
                save_image(place, image_url)
