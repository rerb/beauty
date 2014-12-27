from django.http import JsonResponse
from django.utils.safestring import mark_safe
from django.views.generic import TemplateView
from django.views.generic.base import View

from django_pygments.utils import pygmentify_html


class BeautifulView(View):

    def get(self, request, *args, **kwargs):
        source = self.request.GET['source']
        lang = self.request.GET['lang']
        tagged_source = ('<pre lang="{lang}">'.format(lang=lang) +
                         source +
                         '</pre>')
        pretty_source = pygmentify_html(tagged_source,
                                        noclasses=True)
        safe_source = mark_safe(pretty_source)
        return JsonResponse({'source': safe_source})
