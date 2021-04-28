from django.urls import include
from . import views
from django.urls import path
from .views import *
from django.contrib.sitemaps.views import sitemap
from novels.sitemaps import NovelSitemap, StaticViewSitemap, ShortStorySitemap


sitemaps = {
    'static': StaticViewSitemap,
    'novel': NovelSitemap,
    'story': ShortStorySitemap,
}

urlpatterns = [
    path('', Novels.as_view(), name='novels_list'),
    path('hero-novels/', HeroNovels.as_view(), name='hero_novels'),
    path('genre-novels/', GenreNovels.as_view(), name='genre_novels'),
    path('stories/', views.Stories.as_view(), name='stories'),
    path('novels/<slug:slug>', views.novel_text, name='novel_text'),
    path('stories/<slug:slug>', views.Story.as_view(), name='short_story_text'),
    path('films/', views.Films.as_view(), name='films'),
    path('audiobooks/', Audiobooks.as_view(), name='audiobooks'),
    path('contact/', views.contactView, name='contact_form'),
    path('captcha/', include('captcha.urls')),
    path('show_covers/', DynamicArticleImageView.as_view(), name='show_covers'),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
]


from django.contrib.flatpages import views

urlpatterns += [
    path('biography/', views.flatpage, {'url': '/biography/'}, name='biography'),
]