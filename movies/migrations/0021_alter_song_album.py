# Generated by Django 4.1.1 on 2023-07-11 08:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("movies", "0020_alter_movie_person_name"),
    ]

    operations = [
        migrations.AlterField(
            model_name="song",
            name="album",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT, to="movies.album"
            ),
        ),
    ]