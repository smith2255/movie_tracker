from datetime import datetime, timedelta
from . import models
from model_mommy.recipe import Recipe, seq

movie_titles = [
    'Heat',
    'Michael Clayton',
    'Collateral',
    'The Prestige',
    'Bad Santa',
]

movies_on_the_same_date = Recipe(
    models.Movie,
    title=seq(movie_titles),
    release_date=datetime.date.today(),
    run_time=seq(120),
)
