from django.db import models
from tinymce.models import HTMLField



class Place (models.Model):
    title = models.CharField('Название', max_length=200)
    short_description = models.TextField('Краткое описание', blank=True)
    long_description = HTMLField('Полное описание', blank=True)
    lat = models.FloatField(verbose_name='Широта')
    lon = models.FloatField(verbose_name='Долгота')

    def __str__(self):
        return self.title
    
    class Meta: 
        verbose_name_plural = 'Места'


class Image (models.Model):
    image = models.ImageField('Картинка')
    position = models.IntegerField('Позиция')
    place = models.ForeignKey('Place', on_delete=models.CASCADE, related_name='images')

    def __str__(self):
        view = f'{str(self.position)} {self.place.title}'
        return view
    
    class Meta:
        ordering = ['position'] 
        verbose_name_plural = 'Фотографии'