# Generated by Django 3.1.14 on 2023-03-20 00:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pokemon_entities', '0009_auto_20230319_0320'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pokemonentity',
            old_name='Attack',
            new_name='attack',
        ),
        migrations.RenameField(
            model_name='pokemonentity',
            old_name='Defense',
            new_name='defense',
        ),
        migrations.RenameField(
            model_name='pokemonentity',
            old_name='Health',
            new_name='health',
        ),
        migrations.RenameField(
            model_name='pokemonentity',
            old_name='Level',
            new_name='level',
        ),
        migrations.RenameField(
            model_name='pokemonentity',
            old_name='Stamina',
            new_name='stamina',
        ),
        migrations.AlterField(
            model_name='pokemon',
            name='previous_evolution',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='next_evolutions', to='pokemon_entities.pokemon', verbose_name='Из кого иволюционировал'),
        ),
    ]