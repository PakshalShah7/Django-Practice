# Generated by Django 4.1.1 on 2022-11-14 13:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0018_movie_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='slug',
            field=models.SlugField(blank=True, editable=False, null=True, unique=True),
        ),
        migrations.AlterUniqueTogether(
            name='movie',
            unique_together={('person_name', 'title')},
        ),
    ]