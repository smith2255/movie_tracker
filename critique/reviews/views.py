from django.shortcuts import render
from . import models


def all_movies(request):

    template = 'all_movies.html'
    movies = models.Movie.objects.all()

    return render(
        request,
        template,
        {'movies': movies}
    )
