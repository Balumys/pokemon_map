# Generated by Django 3.1.14 on 2023-03-20 00:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pokemon_entities', '0011_auto_20230320_0052'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pokemonentity',
            name='pokemon',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='pokemon_entities.pokemon', verbose_name='Покемон'),
        ),
    ]