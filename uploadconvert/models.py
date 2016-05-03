from django.db import models
from django.forms import ModelForm
from django.conf import settings
import os
from django.utils.text import slugify


def path_and_rename(instance, filename):
        ext = filename.split('.')[-1]
        filename = '{}.{}'.format(instance.title, ext)
        return os.path.join('uploads', filename)


class Movie(models.Model):
    title = models.CharField(max_length=100)
    title_slug = models.SlugField(max_length=110, default='')
    file = models.FileField(upload_to=path_and_rename)
    uploader = models.ForeignKey(settings.AUTH_USER_MODEL, default=1)

    def __unicode__(self):
        return self.file.name

    def save(self, *args, **kwargs):
        self.title_slug = slugify(self.title)
        super(Movie, self).save(*args, **kwargs)


class MovieForm(ModelForm):
    class Meta:
        model = Movie
        fields = ['title', 'file', ]
