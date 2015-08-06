from django.conf.urls import patterns, include, url
from django.contrib import admin
from news.views import *

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^/?$', 'news.views.news_list', name='news-list'),
    url(r'^news/(?P<slug>[\w\-_]+)/$', 'news.views.news_detail', name='news-detail'),
    url(r'^dodaj_komentarz/$', 'news.views.add_note', name='add-comment'),
)
