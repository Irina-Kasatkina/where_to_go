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
            response = requests.get(json_url)
            response.raise_for_status()

            location_details = response.json()
            place, _ = Place.objects.update_or_create(
                title=location_details['title'],
                defaults={'short_description': location_details['description_short'],
                          'long_description': location_details['description_long'],
                          'longitude': location_details['coordinates']['lng'],
                          'latitude': location_details['coordinates']['lat'],
                          }
            )
            if place:
                for image_url in location_details['imgs']:
                    try:
                        response = requests.get(image_url)
                        response.raise_for_status()
                    except (requests.exceptions.HTTPError, requests.exceptions.MissingSchema):
                        continue

                    image = Image(place=place)
                    file_name = os.path.basename(urlparse(image_url).path)
                    content = ContentFile(response.content)
                    image.image.save(file_name, content, save=True)
                    image.save()
