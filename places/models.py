from django.db import models
from tinymce.models import HTMLField


class Place(models.Model):
    """Локация."""

    title = models.CharField('заголовок', max_length=255, db_index=True, unique=True)
    short_description = models.TextField('короткое описание', blank=True)
    long_description = HTMLField('длинное описание', blank=True)
    longitude = models.FloatField('долгота')
    latitude = models.FloatField('широта')

    class Meta:
        ordering = ['title']
        verbose_name = 'локация'
        verbose_name_plural = 'локации'

    def __str__(self):
        return self.title


class Image(models.Model):
    """Фотография локации."""

    number = models.PositiveIntegerField('сортировка', db_index=True, default=0)
    image = models.ImageField('картинка')

    place = models.ForeignKey(
        Place,
        related_name='images',
        verbose_name='место',
        on_delete=models.CASCADE
    )

    class Meta:
        ordering = ['number']
        verbose_name = 'фотография'
        verbose_name_plural = 'фотографии'
