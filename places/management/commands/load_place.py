import os
from hashlib import md5
from urllib.parse import urlparse

import requests
from django.core.files.base import ContentFile
from django.core.management.base import BaseCommand

from ...models import Image, Place


class Command(BaseCommand):
    help = 'Команда загрузки json-файла с информацией о локации.'

    def add_arguments(self, parser):
        parser.add_argument('json_urls', nargs='+', type=str, help='url-ы json-файлов c описанием локаций.')

    def handle(self, *args, **kwargs):
        for json_url in kwargs['json_urls']:
            try:
                place, created, location_details = self.load_place(json_url)
                if created:
                    self.load_images(place, location_details.get('imgs', []))
            except KeyError:
                continue

    @staticmethod
    def load_place(json_url):
        response = requests.get(json_url)
        response.raise_for_status()

        location_details = response.json()

        place, created = Place.objects.get_or_create(
            title=location_details['title'],
            longitude=location_details['coordinates']['lng'],
            latitude=location_details['coordinates']['lat'],
            defaults={
                'short_description': location_details.get('description_short', ''),
                'long_description': location_details.get('description_long', '')
            }
        )
        return place, created, location_details

    @staticmethod
    def load_images(place, images_urls):
        for image_url in images_urls:
            response = requests.get(image_url)
            response.raise_for_status()

            _, fileext = os.path.splitext(urlparse(image_url).path)
            filename = f'{md5(response.content).hexdigest()}{fileext}'
            content_file = ContentFile(response.content, name=filename)
            Image.objects.create(place=place, image=content_file)
