from django.contrib import admin
from .models import Person, Movie, Song, Album, Artist

admin.site.register(Person)
admin.site.register(Movie)
admin.site.register(Artist)
admin.site.register(Album)
admin.site.register(Song)
