from django.db import models
from django.db.models import Avg
from django.contrib.auth.models import User

class Genre(models.Model):
    name = models.CharField(
        max_length=50,
    )

    def __str__(self):
        return self.name


class Movie(models.Model):
    title = models.CharField(max_length=50)
    release_date = models.DateField()
    run_time = models.PositiveSmallIntegerField()
    description = models.TextField(max_length=200)
    genres = models.ManyToManyField(Genre)

    class Meta:
        ordering = [
            '-release_date',
            '-title',
            '-run_time',
        ]

    def get_reviews(self):
        return self.review_set.filter(
            was_reviewed=True
        )

    def avg_rating(self):
        reviews = self.review_set.filter(
            was_reviewed=True
        )
        ratings = reviews.aggregate(Avg('rating'))
        if ratings.get('rating__avg'):
            val = round(
                ratings.get('rating__avg'),
                1
            )
            return '{0} / 10'.format(val)
        return 'No one has rated this film yet.'

    def print_genres(self):
        ls = []
        for genre in self.genres.all():
            ls.append(genre.name)
        return ', '.join(ls)

    def __str__(self):
        return '{0}({1})'.format(
            self.title,
            self.release_date.year,
        )

class Review(models.Model):
    """
    Essentialy tracks to see if a user watched the movie or not
    """

    movie = models.ForeignKey(Movie)
    user = models.ForeignKey(User)

    was_reviewed = models.BooleanField(default=False)

    details = models.TextField(
        blank=True,
        max_length=200,
    )
    rating = models.PositiveSmallIntegerField(
        choices=[(i, i) for i in range(0, 11)],
        default=0,
    )
    viewed_on = models.DateField()

    class Meta:
        ordering = [
            'movie',
            'viewed_on',
            'rating',
        ]

    def __str__(self):
        return '{0} - {1}'.format(
            self.movie.title,
            self.user.username,
        )
