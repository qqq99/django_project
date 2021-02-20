from django.contrib import admin
from .models import Genre, Movie
# Register your models here.
# customize the Model(Genre) interface in admin page


class GenreAdmin(admin.ModelAdmin):
    # in the genre admin page disply Genre id and name
    list_display = ('id', 'name')


class MovieAdmin(admin.ModelAdmin):
    # if we don't want to show 'date_created' filed when we add movie in the admin interface
    exclude = ('date_created',)
    # here needs , because we have to tell python it's a tuple not a string wrapped in parentsis
    list_display = ('title', 'number_in_stock', 'daily_rate')


admin.site.register(Genre, GenreAdmin)
admin.site.register(Movie, MovieAdmin)
