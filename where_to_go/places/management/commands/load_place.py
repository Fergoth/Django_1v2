from django.core.management.base import BaseCommand
import requests
from places.models import Place, PlaceImage
from django.core.files.base import ContentFile
import os
from urllib.parse import urlparse


def save_image(place, url):
    filepath = urlparse(url).path
    filename = os.path.basename(filepath)
    try:
        response = requests.get(url)
    except requests.exceptions.HTTPError as err:
        print(f'Проблемы с загрузкой данных по {url}', err)
        return
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
        try:
            r = requests.get(url)
            r.raise_for_status()
        except requests.exceptions.HTTPError as err:
            print('Проблемы с загрузкой данных по url', err)
            return
        try:
            js = r.json()
            title = js['title']
            image_urls = js['imgs']
            description_short = js['description_short']
            description_long = js['description_long']
            lng = js['coordinates']['lng']
            lat = js['coordinates']['lat']
        except KeyError as e:
            print('Некорректный формат json', e)
            return
        except requests.exceptions.JSONDecodeError:
            print('По ссылке находится не json файл')
        place, created = Place.objects.get_or_create(
            title=title,
            description_long=description_long,
            description_short=description_short,
            longitude=lng,
            latitude=lat
        )
        if created:
            print('Сохранена локация, сохраняем фотографии..')
            for image_url in image_urls:
                save_image(place, image_url)
            print('Фотографии сохранены')
        else:
            print('Локация уже существует')
