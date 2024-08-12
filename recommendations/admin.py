from django.contrib import admin
from .models import Movie
from .forms import MovieAdminForm

class MovieAdmin(admin.ModelAdmin):
    form = MovieAdminForm

admin.site.register(Movie, MovieAdmin)
