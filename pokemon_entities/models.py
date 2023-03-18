from django.db import models  # noqa F401


class Pokemon(models.Model):
    title = models.CharField(max_length=200)
    photo = models.ImageField(upload_to='pokemon', blank=True)

    def __str__(self):
        return self.title


class PokemonEntity(models.Model):
    pokemon = models.ForeignKey(Pokemon, on_delete=models.CASCADE)
    lat = models.FloatField()
    long = models.FloatField()
    appears_at = models.DateTimeField(null=True, blank=True)
    disappears_at = models.DateTimeField(null=True, blank=True)
    Level = models.CharField(max_length=200,blank=True)
    Health = models.CharField(max_length=200,blank=True)
    Attack = models.CharField(max_length=200,blank=True)
    Defense = models.CharField(max_length=200,blank=True)
    Stamina = models.CharField(max_length=200,blank=True)

    def __str__(self):
        return f"{self.pokemon} lvl {self.Level}"

