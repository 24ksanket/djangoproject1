from django.contrib import admin
from testapp.models import Movie

class MovieAdmin(admin.ModelAdmin):
    list_display = ['rdate','moviename','hero','heroin','rating']

# Register your models here.
admin.site.register(Movie,MovieAdmin)

