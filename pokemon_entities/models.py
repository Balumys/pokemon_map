from django.db import models  # noqa F401


class Pokemon(models.Model):
    title = models.CharField(max_length=200)
    photo = models.ImageField(upload_to='pokemon', blank=True)

    def __str__(self):
        return self.title


class PokemonEntity(models.Model):
    lat = models.FloatField()
    long = models.FloatField()
    pokemon = models.ForeignKey(Pokemon, on_delete=models.CASCADE)
