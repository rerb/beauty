from django.conf.urls import patterns, url

import views


urlpatterns = patterns(
    '',

    url(r'^$',
        views.BeautifulView.as_view(),
        name='beautiful-view'))
