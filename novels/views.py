from django.shortcuts import render
from django.core.paginator import Paginator
from .models import *
from django.core.mail import send_mail
from django.conf import settings
from django.http import JsonResponse
from django.views import View
from django.views.generic import TemplateView
from .filters import AudiobookFilter
import os


class Novels(TemplateView):
    template_name = "novels/novels_list.html"

    def get_context_data(self, **kwargs):
        context = super(Novels, self).get_context_data(**kwargs)
        context['novels'] = Novel.objects.all().order_by('serial_number')
        return context


class HeroNovels(TemplateView):
    template_name = "novels/hero_novels.html"

    def get_context_data(self, **kwargs):
        context = super(HeroNovels, self).get_context_data(**kwargs)
        context['novels'] = Novel.objects.all().order_by('serial_number')
        context['heroes'] = MainCharacter.objects.all().order_by('character')
        context['non_heroes'] = Novel.objects.filter(main_characters__character=None).order_by('serial_number')
        return context


class GenreNovels(TemplateView):
    template_name = "novels/genre_novels.html"

    def get_context_data(self, **kwargs):
        context = super(GenreNovels, self).get_context_data(**kwargs)
        context['genres'] = BookGenre.objects.all().order_by('genre')
        return context


def novel_text(request, slug):
        get_file = Novel.objects.get(slug=slug).novel_txt
        file_path = os.path.join('media', str(get_file))

        with open(file_path) as f:
            lines = f.readlines()

        novels = Novel.objects.get(slug=slug).title_rus
        description = Novel.objects.get(slug=slug).description
        paginator = Paginator(lines, 30)
        page = request.GET.get('page')
        plines = paginator.get_page(page)

        context = {
            'novels': novels,
            'plines': plines,
            'description': description,
        }

        return render(request, 'novels/text.html', context)



class Stories(TemplateView):
    template_name = "novels/short_story_list.html"

    def get_context_data(self, **kwargs):
        context = super(Stories, self).get_context_data(**kwargs)
        context['stories'] = ShortStory.objects.all().order_by('serial_number')
        return context


class Story(TemplateView):
    template_name = "novels/short_story.html"

    def get_context_data(self, **kwargs):
        context = super(Story, self).get_context_data(**kwargs)
        context['stories'] = ShortStory.objects.get(slug=self.kwargs.get('slug', None)).content
        context['name_stories'] = ShortStory.objects.get(slug=self.kwargs.get('slug', None)).name_story_rus
        return context


class Films(TemplateView):
    template_name = "novels/films.html"

    def get_context_data(self, **kwargs):
        context = super(Films, self).get_context_data(**kwargs)
        context['films'] = Film.objects.all().order_by('title_rus')
        return context


class Audiobooks(TemplateView):
    template_name = "novels/audiobooks_list.html"

    def get_context_data(self, **kwargs):
        context = super(Audiobooks, self).get_context_data(**kwargs)
        context['filter'] = AudiobookFilter(self.request.GET, queryset=Audiobook.objects.all())
        return context


def contactView(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        # Если форма заполнена корректно, сохраняем все введённые пользователем значения
        if form.is_valid():
            subject = form.cleaned_data['subject']
            sender = form.cleaned_data['sender']
            message = form.cleaned_data['message']
            recipients = [settings.EMAIL_HOST_USER]
            send_mail('jchase - ' + subject, message, settings.EMAIL_HOST_USER, recipients)
            return render(request, 'forms/thanks.html')

    else:
        # Заполняем форму
        form = ContactForm()
    # Отправляем форму на страницу
    return render(request, 'forms/contact.html', {'form': form})


class DynamicArticleImageView(View):

    def get(self, *args, **kwargs):
        article_id = self.request.GET.get('article_id')
        image_id = self.request.GET.get('article_id')
        article = Novel.objects.get(slug=article_id)
        image = Cover.objects.values('cover').filter(name_cover=image_id)
        image_list = {'image': list(image)}
        data = {
            'article_id': article.serial_number,
            'image': image_list
        }
        return JsonResponse(data)

