from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
                       url(r'^admin/', include(admin.site.urls)),
                       url(r'^beauty/', include('apps.beauty.urls',
                                                namespace='beauty',
                                                app_name='Beauty')))
