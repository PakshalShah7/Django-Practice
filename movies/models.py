from django.db import models
from django.utils.text import slugify


class Person(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class MovieManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().get(title__icontains='movie1')


class Movie(models.Model):
    title = models.CharField(max_length=50)
    release_date = models.DateField()
    description = models.CharField(max_length=200)
    person_name = models.ForeignKey(Person, on_delete=models.CASCADE, null=True, blank=True, related_name='movies')
    slug = models.SlugField(unique=True, null=True, blank=True, editable=False)
    objects = models.Manager()
    movies = MovieManager()

    class Meta:
        unique_together = ['person_name', 'title']
        # unique_constraints = models.UniqueConstraint(fields=['person_name', 'title'])

    def __str__(self):
        return self.title

    def save(self, *args):
        self.slug = slugify(self.title)
        return super().save(*args)


class Artist(models.Model):
    artist_name = models.CharField(max_length=10)

    def __str__(self):
        return self.artist_name


class Album(models.Model):
    album_name = models.CharField(max_length=50)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)

    def __str__(self):
        return self.album_name


class Song(models.Model):
    song_name = models.CharField(max_length=30)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    album = models.ForeignKey(Album, on_delete=models.PROTECT)

    def __str__(self):
        return self.song_name
