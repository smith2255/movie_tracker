from django.contrib import admin

# Register your models here.
from . import models

admin.site.register(models.Movie)
admin.site.register(models.Review)
admin.site.register(models.Genre)
