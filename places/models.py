from django.db import models


class Place(models.Model):
    """Место."""

    title = models.CharField('заголовок', max_length=50, db_index=True, unique=True)
    short_description = models.TextField('короткое описание')
    long_description = models.TextField('длинное описание')
    longitude = models.FloatField('долгота')
    latitude = models.FloatField('широта')

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['title']
        verbose_name = 'место'
        verbose_name_plural = 'места'


class Image(models.Model):
    """Картинка места."""

    number = models.IntegerField('порядковый номер')
    image = models.ImageField('картинка')

    place = models.ForeignKey(
        Place,
        related_name='images',
        verbose_name='место',
        on_delete=models.CASCADE
    )

    class Meta:
        ordering = ['number']
        verbose_name = 'картинка'
        verbose_name_plural = 'картинки'
