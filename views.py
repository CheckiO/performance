from django.views.generic.base import TemplateView


class BlankPage(TemplateView):
    template_name = 'blank.html'


class EmptyPage(TemplateView):
    template_name = 'empty.html'
