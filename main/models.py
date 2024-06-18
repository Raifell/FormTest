from django.db import models
from django.urls import reverse
from django.utils.text import slugify


def album_directory_path(instance, filename):
    return 'album_screen/{}/{}'.format(instance.name, filename)


class Album(models.Model):
    class Status(models.IntegerChoices):
        DRAFT = 0, 'Draft'
        PUBLISHED = 1, 'Published'

    name = models.CharField(max_length=255, verbose_name='Title')
    photo = models.ImageField(upload_to=album_directory_path, blank=True, verbose_name='Photo')
    ready = models.BooleanField(verbose_name='Ready', choices=tuple(map(lambda x: (bool(x[0]), x[1]), Status.choices)),
                                default=Status.DRAFT)
    slug = models.SlugField(max_length=255, verbose_name='Slug', blank=True)

    def __str__(self):
        return self.name

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        self.slug = slugify(self.name + '-slug')
        super(Album, self).save(force_insert, force_update, using, update_fields)

    def get_absolute_url(self):
        return reverse('album', kwargs={'band_slug': self.slug})


def track_directory_path(instance, filename):
    return 'music/{}/{}'.format(instance.album.name, filename)


class Track(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE, verbose_name='Album', null=True)
    url = models.FileField(upload_to=track_directory_path, verbose_name='Track')

    def __str__(self):
        return self.url.url
