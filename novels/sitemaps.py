from django.contrib.sitemaps import Sitemap
from novels.models import Novel, ShortStory
from django.urls import reverse


class StaticViewSitemap(Sitemap):
    priority = 0.9
    changefreq = 'monthly'

    def items(self):
        return ['novels_list', 'hero_novels', 'genre_novels', 'stories', 'films', 'audiobooks', 'contact_form',
                'biography']

    def location(self, item):
        return reverse(item)


class NovelSitemap(Sitemap):
    changefreq = "monthly"
    priority = 0.5

    def items(self):
        return Novel.objects.order_by('serial_number')


class ShortStorySitemap(Sitemap):
    changefreq = "monthly"
    priority = 0.5

    def items(self):
        return ShortStory.objects.order_by('serial_number')
