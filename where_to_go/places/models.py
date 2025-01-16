from django.db import models


class Place(models.Model):
    title = models.CharField("Заголовок", max_length=200)
    description_short = models.TextField("Краткое описание")
    description_long = models.TextField("Полное описание")
    latitude = models.DecimalField("Широта", max_digits=9, decimal_places=6)
    longitude = models.DecimalField("Долгота", max_digits=9, decimal_places=6)

    class Meta:
        verbose_name = 'место'
        verbose_name_plural = 'места'

    def __str__(self):
        return self.title


class Image(models.Model):
    place = models.ForeignKey(
        Place,
        on_delete=models.DO_NOTHING,
        related_name='images',
        verbose_name='Локация',
        null=True,
        blank=True
    )
    image = models.ImageField()
    order = models.IntegerField()

    class Meta:
        ordering = ['order']
        verbose_name = 'картинка'
        verbose_name_plural = 'картинки'

    def __str__(self):
        return f"{self.order} {self.place.title}"
