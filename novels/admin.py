from django.contrib import admin
from .models import *


class NovelAdmin(admin.ModelAdmin):
    list_display = ("serial_number", "title_rus", "title_eng", "book_genre")
    list_display_links = ("title_rus", "title_eng")
    search_fields = ("title_rus", "title_eng", "book_genre")
    filter_horizontal = ('audiobooks', 'covers', 'main_characters')
    prepopulated_fields = {"slug": ("title_eng",)}
    fieldsets = (
        (None, {
            'fields': ('serial_number', 'year')
        }),
        ('Title', {
            'fields': ('title_eng', ('alternative_title_eng_1',
                                     'alternative_title_eng_2',
                                     'alternative_title_eng_3',),
                       'title_rus',
                       ('alternative_title_rus_1',
                        'alternative_title_rus_2',
                        'alternative_title_rus_3',),
                       ('alternative_title_rus_4',
                        'alternative_title_rus_5',
                        'alternative_title_rus_6',),
                       ('alternative_title_rus_7',
                        'alternative_title_rus_8',
                        'alternative_title_rus_9',),
                       ('alternative_title_rus_10',
                        'alternative_title_rus_11')
                       )
        }),
        ('Details', {
            'fields': ('location', 'book_genre', 'main_characters', 'description')
        }),

        # ('Details', {
        #     'fields': ('location', 'main_characters', 'description')
        # }),

        ('Books', {
            'fields': ('books_rus_epub',
                       'books_rus_fb2',
                       'books_rus_pdf',
                       'books_rus_djvu',
                       'books_eng_epub',
                       'books_eng_pdf',
                       'books_eng_djvu',
                       'books_fr_epub',
                       'books_fr_pdf',
                       'books_it_pdf',)
        }),
        ('Audiobooks', {
            'fields': ('audiobooks',)
        }),
        ('Covers', {
            'fields': ('slug', 'covers')
        }),
        ('Text-file', {
            'fields': ('novel_txt',)
        })
    )


admin.site.register(Novel, NovelAdmin)


class CoverAdmin(admin.ModelAdmin):
    list_display = ("cover", "image_img")
    readonly_fields = ("image_img",)
    search_fields = ("name_cover",)


admin.site.register(Cover, CoverAdmin)


class ShortStoryAdmin(admin.ModelAdmin):
    list_display = ("serial_number", "name_story_rus", "name_story_eng")


admin.site.register(ShortStory, ShortStoryAdmin)


class AudiobookAdmin(admin.ModelAdmin):
    fields = (('title', 'author'), ('bitrate', 'running_time', 'release_date'), ('links'))
    list_display = ("title", "author", "bitrate")
    search_fields = ("title",)
    autocomplete_fields = ['author']


admin.site.register(Audiobook, AudiobookAdmin)


class AuthorAudiobookAdmin(admin.ModelAdmin):
    list_display = ("author",)
    search_fields = ("author",)


admin.site.register(AuthorAudiobook, AuthorAudiobookAdmin)


class FilmAdmin(admin.ModelAdmin):
    list_display = ("title_rus", "title_eng", "according_to_the_novel")
    list_display_links = ("title_rus", "title_eng")
    search_fields = ("title_rus", "title_eng")


class BookGenreAdmin(admin.ModelAdmin):
    list_display = ("genre",)
    search_fields = ("genre",)


admin.site.register(BookGenre, BookGenreAdmin)
admin.site.register(Film, FilmAdmin)
admin.site.register(MainCharacter)
