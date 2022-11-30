from django.db import models


class Pokemon(models.Model):
    title = models.TextField(verbose_name='Наименование на русском')
    title_jp = models.TextField(verbose_name='Наименование на японском', blank=True)
    title_en = models.TextField(verbose_name='Наименование на английском', blank=True)
    image = models.ImageField(null=True, blank=True, verbose_name='Изображение')
    description = models.TextField(max_length=1000, verbose_name='Описание', blank=True)

    previous_evolution = models.ForeignKey('self', on_delete=models.SET_NULL,
        null=True, blank=True, related_name='next_evolution', verbose_name='Из кого эволюционировал')

    def __str__(self):
        return str(self.title)


class PokemonEntity(models.Model):
    lat = models.FloatField(null=True, verbose_name='Широта')
    lon = models.FloatField(null=True, verbose_name='Долгота')

    appeared_at = models.DateTimeField(null=True, verbose_name='Появился')
    disappeared_at = models.DateTimeField(null=True, verbose_name ='Исчез')

    level = models.IntegerField(null=True, verbose_name='Уровень')
    health = models.IntegerField(null=True, verbose_name='Здоровье')
    strength = models.IntegerField(null=True, verbose_name='Сила')
    defence = models.IntegerField(null=True, verbose_name='Защита')
    stamina = models.IntegerField(null=True, verbose_name='Выносливость')

    pokemon = models.ForeignKey(
        Pokemon,
        on_delete=models.CASCADE,
        related_name='pokentity')
