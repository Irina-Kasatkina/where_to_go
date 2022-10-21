import os
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
            place, location_details = None, None
            try:
                place, location_details = self.load_place(json_url)
            except KeyError:
                continue

            if place:
                try:
                    self.load_images(place, location_details)
                except KeyError:
                    continue

    @staticmethod
    def load_place(json_url):
        response = requests.get(json_url)
        response.raise_for_status()

        location_details = response.json()

        title = location_details['title']
        try:
            Place.objects.get(title=title)
            return None, None
        except Place.DoesNotExist:
            place = Place.objects.create(
                title=title,
                short_description=location_details['description_short'],
                long_description=location_details['description_long'],
                longitude=location_details['coordinates']['lng'],
                latitude=location_details['coordinates']['lat']
            )
            return place, location_details

    @staticmethod
    def load_images(place, location_details):
        images_urls = location_details['imgs']
        for image_url in images_urls:
            response = requests.get(image_url)
            response.raise_for_status()

            image = Image(place=place)
            filename = os.path.basename(urlparse(image_url).path)
            image.image.save(filename, ContentFile(response.content), save=True)
            image.save()
