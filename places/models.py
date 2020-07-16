from django.db import models


class Place (models.Model):
    title = models.CharField('Название', max_length=200)
    description_short = models.TextField('Краткое описание')
    description_long = models.TextField('Полное описание')
    lat = models.FloatField(verbose_name='Широта')
    lon = models.FloatField(verbose_name='Долгота')

    def __str__(self):
        return self.title


class Image (models.Model):
    image = models.ImageField('Картинка')
    position = models.IntegerField('Позиция')
    place = models.ForeignKey('Place', on_delete=models.CASCADE, related_name='images')

    def __str__(self):
        view = f'{str(self.position)} {self.place.title}'
        return view