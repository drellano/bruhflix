from django.contrib import admin
from .models import Movie


class MovieAdmin(admin.ModelAdmin):
    change_form_template = 'progressbarupload/change_form.html'
    add_form_template = 'progressbarupload/change_form.html'

admin.site.register(Movie, MovieAdmin)
