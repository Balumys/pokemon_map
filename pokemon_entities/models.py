from django.db import models  # noqa F401


class Pokemon(models.Model):
    """Покемон"""
    title = models.CharField('Имя', max_length=200)
    title_en = models.CharField('Имя англ', max_length=200, blank=True)
    title_jp = models.CharField('Имя яп', max_length=200, blank=True)
    photo = models.ImageField('Изображение', upload_to='pokemon', blank=False)
    description = models.TextField('Описание', blank=True)
    previous_evolution = models.ForeignKey('self', verbose_name='Из кого эволюционировал', null=True, blank=True,
                                           on_delete=models.SET_NULL,
                                           related_name='next_evolutions')

    def __str__(self):
        return self.title


class PokemonEntity(models.Model):
    """Свойство покемона и информация о времени и месте появления"""
    pokemon = models.ForeignKey(Pokemon, on_delete=models.PROTECT, verbose_name='Покемон', related_name='pokemon_spawns')
    lat = models.FloatField('Широта')
    long = models.FloatField('Долгота')
    appears_at = models.DateTimeField('Время появления', null=True, blank=False)
    disappears_at = models.DateTimeField('Время исчезновения', null=True, blank=False)
    level = models.CharField('Уровень', max_length=200, blank=True)
    health = models.CharField('Здоровье', max_length=200, blank=True)
    attack = models.CharField('Атака', max_length=200, blank=True)
    defense = models.CharField('Защита', max_length=200, blank=True)
    stamina = models.CharField('Выносливость', max_length=200, blank=True)

    def __str__(self):
        return f"{self.pokemon} lvl {self.level}"
