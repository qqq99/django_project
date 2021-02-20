from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from .models import Movie
# Create your views here.


def index(request):
    ''' # SELECT * FROM movies_movie WHERE release_year = 1989
    Movie.objects.filter(release_year=1989)
    # Movie.objects.get(id=1) '''
    # SELECT * FROM movies_movie
    movies = Movie.objects.all()
    ''' output = ','.join([m.title for m in movies])
    return HttpResponse(output)  '''
    return render(request, 'movies/index.html', {'movies': movies})


# in urls.py we use movie_id as parameter, when user send request to movies/1, django will automatically extract 1, and then it will call this view function and pass 1 as argument
def detail(request, movie_id):
    # return HttpResponse(movie_id)
    ''' try:
        movie = Movie.objects.get(pk=movie_id)
        return render(request, 'movies/detail.html', {'movie': movie})
    # DoesNotExist is part of our Movie Model who inherent models.Model
    except Movie.DoesNotExist:
        raise Http404() '''
    movie = get_object_or_404(Movie, pk=movie_id)
    return render(request, 'movies/detail.html', {'movie': movie})
