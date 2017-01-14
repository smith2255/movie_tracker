from django.conf import settings
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.views import generic

from . import models, forms

import datetime


def default_url_redirect(request):
    return HttpResponseRedirect(
        reverse('reviews:list_movies')
    )

def register(request):
    form = forms.RegistrationForm()
    template = 'registration/register.html'

    # In case a user is logged in
    logout(request)

    if request.method == 'POST':
        form = forms.RegistrationForm(request.POST)

        if form.is_valid():
            form.save()
            
            return HttpResponseRedirect(
                reverse('reviews:list_movies')
            )

    return render(
        request,
        template,
        {'form':form},
    )


@login_required()
def list_movies(request, page_id=1):

    template = 'list_movies.html'
    
    paginator = Paginator(
        models.Movie.objects.all(),
        settings.PAGINATION_SIZE
    )

    movies = None
    try:
        movies = paginator.page(page_id)
    except (PageNotAnInteger, EmptyPage):
        movies = paginator.page(1)


    # makes it easier to display if the request user has seen this film
    for movie in movies:
        review = movie.review_set.filter(user=request.user).count()
        setattr(movie, 'review', review)

    return render(
        request,
        template,
        {'movies': movies}
    )

@login_required()
def details_movie(request, pk):
    template = 'details_movie.html'
    movie = models.Movie.objects.get(pk=pk)
    review = models.Review.objects.filter(
        movie=movie,
        user=request.user
    ).first()

    return render(
        request,
        template,
        {
            'user_review': review,
            'movie': movie
        }
    )

@login_required()
def add_review(request, pk):
    form = forms.ReviewForm(
        initial={
            'viewed_on': datetime.date.today()
        }
    )

    template = 'add_edit_review.html'
    movie = get_object_or_404(models.Movie, pk=pk)

    if request.method == 'POST':

        form = forms.ReviewForm(request.POST)

        if form.is_valid():
            review = form.save(commit=False)
            
            if not review.was_reviewed:
                review.rating = 0
                review.details = ''
            review.movie = movie
            review.user = request.user
            review.save()

            return HttpResponseRedirect(
                reverse('reviews:list_movies')
            )

    return render(
        request,
        template,
        {
            'form': form,
            'movie': movie,
        },
    )


@login_required()
def edit_review(request, pk):

    template = 'add_edit_review.html'
    movie = get_object_or_404(models.Movie, pk=pk)
    review = movie.review_set.filter(user=request.user).first()
    form = forms.ReviewForm(instance=review)

    # if the review doesn't exist, just re-direct them so they can add one
    if not review:
        return HttpResponseRedirect(
            reverse(
                'reviews:add_review',
                kwargs={'pk':movie.id}
            )
        )

    if request.method == 'POST':
        form = forms.ReviewForm(request.POST, instance=review)

        if form.is_valid():
            review = form.save(commit=False)
            
            if not review.was_reviewed:
                review.rating = 0
                review.details = ''
            review.save()
            
            return HttpResponseRedirect(
                reverse(
                    'reviews:details_movie',
                    kwargs={'pk':movie.id},
                )
            )

    return render(
        request,
        template,
        {
            'form': form,
            'movie': movie,
            'review': review,
        },
    )
