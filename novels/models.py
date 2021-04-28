from django.db import models
from hashlib import md5
from os import path as op
from time import time
from django.db.models.signals import post_delete
from django import forms
from django.utils.html import format_html
from captcha.fields import CaptchaField
from uuslug import slugify


def delete_image(sender, **kwargs):
    # функция удаления изображений при удалении объектов
    try:
        object_ = kwargs.get('instance')
        storage, path = object_.cover.storage, object_.cover.path
        storage.delete(path)
    except:
        pass


class Novel(models.Model):
    serial_number = models.IntegerField()
    slug = models.SlugField()
    year = models.CharField(max_length=4)
    title_eng = models.CharField(max_length=100)
    title_rus = models.CharField(max_length=100)
    alternative_title_eng_1 = models.CharField(max_length=100, blank=True, null=True)
    alternative_title_eng_2 = models.CharField(max_length=100, blank=True, null=True)
    alternative_title_eng_3 = models.CharField(max_length=100, blank=True, null=True)
    alternative_title_rus_1 = models.CharField(max_length=100, blank=True, null=True)
    alternative_title_rus_2 = models.CharField(max_length=100, blank=True, null=True)
    alternative_title_rus_3 = models.CharField(max_length=100, blank=True, null=True)
    alternative_title_rus_4 = models.CharField(max_length=100, blank=True, null=True)
    alternative_title_rus_5 = models.CharField(max_length=100, blank=True, null=True)
    alternative_title_rus_6 = models.CharField(max_length=100, blank=True, null=True)
    alternative_title_rus_7 = models.CharField(max_length=100, blank=True, null=True)
    alternative_title_rus_8 = models.CharField(max_length=100, blank=True, null=True)
    alternative_title_rus_9 = models.CharField(max_length=100, blank=True, null=True)
    alternative_title_rus_10 = models.CharField(max_length=100, blank=True, null=True)
    alternative_title_rus_11 = models.CharField(max_length=100, blank=True, null=True)
    location = models.CharField(max_length=50)
    book_genre = models.ForeignKey('BookGenre', blank=True, null=True, on_delete=models.CASCADE)
    main_characters = models.ManyToManyField('MainCharacter', blank=True)
    description = models.TextField(blank=True)
    books_rus_epub = models.FileField(upload_to='novels/books/books_rus_epub', blank=True, null=True)
    books_rus_fb2 = models.FileField(upload_to='novels/books/books_rus_fb2', blank=True, null=True)
    books_rus_pdf = models.FileField(upload_to='novels/books/books_rus_pdf', blank=True, null=True)
    books_rus_djvu = models.FileField(upload_to='novels/books/books_rus_djvu', blank=True, null=True)
    books_eng_epub = models.FileField(upload_to='novels/books/books_eng_epub', blank=True, null=True)
    books_eng_pdf = models.FileField(upload_to='novels/books/books_eng_pdf', blank=True, null=True)
    books_eng_djvu = models.FileField(upload_to='novels/books/books_eng_djvu', blank=True, null=True)
    books_fr_epub = models.FileField(upload_to='novels/books/books_fr_epub', blank=True, null=True)
    books_fr_pdf = models.FileField(upload_to='novels/books/books_fr_pdf', blank=True, null=True)
    books_it_pdf = models.FileField(upload_to='novels/books/books_it_pdf', blank=True, null=True)
    audiobooks = models.ManyToManyField('Audiobook', blank=True)
    covers = models.ManyToManyField('Cover', blank=True)
    novel_txt = models.FileField(upload_to='novels/books/books_rus_txt', blank=True, null=True)

    def get_films(self):
        return self.film_set.all()

    def get_absolute_url(self):
        return "/%s/" % self.slug

    def __str__(self):
        return '%s %s %s %s %s' % (self.serial_number, " - ", self.title_eng, " - ", self.title_rus)


class BookGenre(models.Model):
    genre = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.genre


class MainCharacter(models.Model):
    character = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.character


class Audiobook(models.Model):
    title = models.CharField(max_length=100, blank=True, null=True)
    author = models.ForeignKey('AuthorAudiobook', blank=True, null=True, on_delete=models.CASCADE)
    running_time = models.CharField(max_length=5, blank=True, null=True)
    release_date = models.CharField(max_length=4, blank=True, null=True)
    bitrate = models.CharField(max_length=4, blank=True, null=True)
    links = models.URLField(max_length=200, blank=True)

    def __str__(self):
        return '%s %s %s' % (self.title, " - ", self.author)


class AuthorAudiobook(models.Model):
    author = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.author


def film_cover_upload(instance, filename, unique=False):
    """ Auto generate for Image fields"""
    ext = op.splitext(filename)[1]
    name = str(instance.pk or '') + filename + (str(time()) if unique else '')
    filename_unique = slugify(instance.title_rus) + '-' + md5(name.encode('utf8')).hexdigest() + ext
    basedir = op.join(instance._meta.app_label)
    return op.join(basedir, 'films', filename_unique)


class Film(models.Model):
    title_rus = models.CharField(max_length=100, blank=True, null=True)
    title_eng = models.CharField(max_length=100, blank=True)
    genre = models.CharField(max_length=50, blank=True, null=True)
    director = models.CharField(max_length=100, blank=True, null=True)
    release_date = models.CharField(max_length=4, blank=True, null=True)
    running_time = models.CharField(max_length=4, blank=True, null=True)
    description = models.TextField(blank=True)
    country = models.CharField(max_length=100, blank=True, null=True)
    according_to_the_novel = models.ForeignKey('Novel', blank=True, null=True, on_delete=models.CASCADE)
    links = models.URLField(max_length=200, blank=True)
    film_cover = models.ImageField(upload_to=film_cover_upload, blank=True, null=True)

    def __str__(self):
        return self.title_rus


def upload_to(instance, filename, unique=False):
    """ Auto generate name for File and Image fields"""
    ext = op.splitext(filename)[1]
    name = str(instance.pk or '') + filename + (str(time()) if unique else '')
    filename = slugify(instance.name_cover)
    filename_unique = slugify(instance.name_cover) + '-' + md5(name.encode('utf8')).hexdigest() + ext
    basedir = op.join(instance._meta.app_label)
    return op.join(basedir, 'novel_cover', filename, filename_unique)


class Cover(models.Model):
    name_cover = models.CharField(max_length=100, blank=True, null=True)
    cover = models.ImageField(upload_to=upload_to)

    def image_img(self):
        return format_html(u'<img src="%s" height=100/>' % str(self.cover.url))

    image_img.short_description = 'Изображение'
    image_img.allow_tags = True

    def __str__(self):
        return self.cover.url


class ShortStory(models.Model):
    serial_number = models.IntegerField()
    name_story_eng = models.CharField(max_length=100)
    name_story_rus = models.CharField(max_length=100)
    slug = models.SlugField()
    content = models.TextField()

    def get_absolute_url(self):
        return "/%s/" % self.slug


class ContactForm(forms.Form):
    subject = forms.CharField(min_length=2, max_length=100)
    sender = forms.EmailField()
    message = forms.CharField(max_length=1000, widget=forms.Textarea)
    captcha = CaptchaField()


post_delete.connect(receiver=delete_image, sender=Cover)
