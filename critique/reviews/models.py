from django.db import models
from django.contrib.auth.models import User


class Genre(models.Model):
    name = models.CharField(
        max_length=50,
    )

    def __str__(self):
        return self.name


class Movie(models.Model):
    title = models.CharField(
        max_length=50,
    )
    release_date = models.DateField()
    run_time = models.PositiveSmallIntegerField()
    description = models.TextField(
        max_length=200,
    )
    genres = models.ManyToManyField(Genre)

    class Meta:
        ordering = [
            'release_date',
            'title',
            'run_time',
        ]

    def print_genres(self):
        return str(list(self.genres.objects.all()))


    def __str__(self):
        return '{0}({1})'.format(
            self.title,
            self.release_date.year,
        )


class Viewing(models.Model):
    movie = models.ForeignKey(Movie)
    user = models.ForeignKey(User)
    viewed_on = models.DateField()
    rating = models.PositiveSmallIntegerField(
        choices=[(i, i) for i in range(1, 11)],
    )
    review = models.TextField(
        blank=True,
        max_length=200,
    )

    class Meta:
        ordering = [
            'movie',
            'rating',
        ]

    def __str__(self):
        return '{0} {1}'.format(
            self.movie,
            self.rating,
        )
