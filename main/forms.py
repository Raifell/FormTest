from django import forms

from main.models import Album, Track


class AddAlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = ['name', 'photo']


class AddTrackForm(forms.ModelForm):
    class Meta:
        model = Track
        exclude = ('album',)
