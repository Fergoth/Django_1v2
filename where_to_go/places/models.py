from django.db import models
from tinymce.models import HTMLField


class Place(models.Model):
    title = models.CharField("Заголовок", max_length=200)
    description_short = models.TextField("Краткое описание")
    description_long = HTMLField("Полное описание")
    latitude = models.DecimalField("Широта", max_digits=9, decimal_places=6)
    longitude = models.DecimalField("Долгота", max_digits=9, decimal_places=6)

    class Meta:
        verbose_name = 'место'
        verbose_name_plural = 'места'

    def __str__(self):
        return self.title


class PlaceImage(models.Model):
    place = models.ForeignKey(
        Place,
        on_delete=models.CASCADE,
        related_name='images',
        verbose_name='Локация',
        null=True,
        blank=True
    )
    image = models.ImageField('Файл картинки')
    order = models.PositiveIntegerField(
        verbose_name='Порядковый номер',
        db_index=True,
        default=0,
        blank=False,
        null=False
    )

    class Meta:
        ordering = ['order']
        verbose_name = 'картинка'
        verbose_name_plural = 'картинки'

    def __str__(self):
        return f"{self.order} {self.place.title}"
