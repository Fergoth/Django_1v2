import os
from urllib.parse import urlparse

import requests
from django.core.files.base import ContentFile
from django.core.management.base import BaseCommand

from places.models import Place, PlaceImage


def save_image(place, url):
    filepath = urlparse(url).path
    filename = os.path.basename(filepath)
    try:
        response = requests.get(url)
    except requests.exceptions.HTTPError as err:
        print(f'Проблемы с загрузкой данных по {url}', err)
        return
    imagefile = ContentFile(response.content, filename)
    PlaceImage.objects.create(
        place=place,
        image=imagefile
    )


class Command(BaseCommand):
    help = 'Загрузка мест'

    def add_arguments(self, parser):
        parser.add_argument('url', help='Url до json файла')

    def handle(self, *args, **options):
        url = options['url']
        try:
            response = requests.get(url)
            response.raise_for_status()
        except requests.exceptions.HTTPError as err:
            print('Проблемы с загрузкой данных по url', err)
            return
        try:
            place_raw = response.json()
            title = place_raw['title']
            image_urls = place_raw['imgs']
            short_description = place_raw['description_short']
            long_description = place_raw['description_long']
            lng = place_raw['coordinates']['lng']
            lat = place_raw['coordinates']['lat']
        except KeyError as e:
            print('Некорректный формат json', e)
            return
        except requests.exceptions.JSONDecodeError:
            print('По ссылке находится не json файл')
        place, created = Place.objects.get_or_create(
            title=title,
            defaults={
                'long_description': long_description,
                'short_description': short_description,
                'longitude': lng,
                'latitude': lat
            }
        )
        if created:
            print('Сохранена локация, сохраняем фотографии..')
            for image_url in image_urls:
                save_image(place, image_url)
            print('Фотографии сохранены')
        else:
            print('Локация уже существует')
