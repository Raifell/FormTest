from django.forms import formset_factory
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import FormView, TemplateView

from main.forms import AddAlbumForm, AddTrackForm
from main.models import Track, Album


def main_page(request):
    data = {
        'title': 'Main'
    }
    return render(request, 'main_page.html', data)


MyFormSet = formset_factory(AddAlbumForm, AddTrackForm)


class FormPage(TemplateView):
    template_name = 'form_page.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Form'
        context['form_one'] = AddAlbumForm()
        context['form_two'] = AddTrackForm()
        return context

    def post(self, request, *args, **kwargs):
        album_form = AddAlbumForm(request.POST, request.FILES)

        if album_form.is_valid():
            album = Album.objects.filter(name=album_form.cleaned_data['name'])
            if not album:
                album_form.save()
                data = {x: request.FILES[x] for x in request.FILES if 'url' in x}

                for i in data:
                    obj = Track(
                        album=Album.objects.get(name=album_form.cleaned_data['name']),
                        url=data[i]
                    )
                    obj.save()
                return HttpResponse("Forms submitted successfully!")
            else:
                return HttpResponse("Album is already exists!")

        else:
            return self.render_to_response(self.get_context_data())

