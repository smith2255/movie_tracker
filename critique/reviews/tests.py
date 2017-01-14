from . import models
from django.test import TestCase
from model_mommy import mommy

import datetime


class Test_Genre_Model(TestCase):

    def setUp(self):
        self.genre = mommy.make(
            'reviews.Genre',
            name='Documentary',
        )

    def test_basic_functionality(self):
        self.assertEqual(
            str(self.genre),
            'Documentary'
        )


class Test_Movie_Model(TestCase):

    def setUp(self):
        self.movies = mommy.make(
            'reviews.Movie',
            make_m2m=True,
            _quantity=15,
        )

    def test_customized_order(self):
        order_list = list(models.Movie.objects.all().order_by(
            '-release_date',
            '-title',
            '-run_time',
        ))
        self.assertListEqual(
            list(models.Movie.objects.all()),
            order_list,
        )

    def test_customized_string_method(self):
        release_date = datetime.date(1976, 11, 21)
        movie = mommy.make(
            'reviews.Movie',
            release_date=release_date,
            title='Rocky',
            make_m2m=True,
        )
        self.assertEqual(
            str(movie),
            'Rocky(1976)',
        )


class Test_Review_Model(TestCase):

    def setUp(self):
        self.movies = mommy.make(
            'reviews.Review',
            make_m2m=True,
            _quantity=12,
        )

    def test_customized_order(self):
        order_list = list(models.Review.objects.all().order_by(
            'movie',
            'viewed_on',
            'user__username',
        ))

        self.assertListEqual(
            list(models.Review.objects.all()),
            order_list,
        )

    def test_customized_string_method(self):
        review = mommy.make(
            'reviews.Review',
            make_m2m=True,
        )

        ret_str = '{0} - {1}'.format(
            review.movie.title,
            review.user.username,
        )

        self.assertEqual(
            str(review),
            ret_str
        )
