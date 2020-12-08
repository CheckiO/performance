import django_filters

from django.contrib.auth.models import User

from apps.rest_api.filters import CharFilter, IStartsWithFilter

from apps.profiles.models import ElementTipUser


class ElementTipsFiltering(django_filters.FilterSet):
    is_seen = django_filters.BooleanFilter()
    page_slug = CharFilter('tip__page_slug')

    class Meta:
        model = ElementTipUser
        fields = ['is_seen', 'page_slug']


class UserFilter(django_filters.FilterSet):
    username = IStartsWithFilter()

    class Meta:
        model = User
        fields = ('username',)
        order_by = ('username',)
