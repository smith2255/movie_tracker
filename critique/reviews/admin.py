from django.contrib import admin

# Register your models here.
from . import models

admin.site.register(models.Movie)
admin.site.register(models.Viewing)
admin.site.register(models.Genre)
