import django_filters
from .models import *


class AudiobookFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(lookup_expr='icontains')
    author = django_filters.ModelChoiceFilter(queryset=AuthorAudiobook.objects.all())

    class Meta:
        model = Audiobook
        fields = ['title', 'author', ]
