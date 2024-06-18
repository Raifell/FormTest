from django.contrib import admin

from main.models import Album, Track


@admin.register(Track)
class AdminTrack(admin.ModelAdmin):
    list_display = ['url', 'album']


admin.site.register(Album)

