from django.conf.urls import patterns, include, url
from django.contrib import admin
from .views import NewsDetailView, NewsList
from .feeds import ArchieveFeed

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^/?$', NewsList.as_view(), name='news-list'),
    url(r'^(?P<page>[0-9]+)/$', NewsList.as_view(), name='news-list'),
    url(r'^news/(?P<slug>[\w\-_]+)/$', NewsDetailView.as_view(),
        name='news-detail'),
    url(r'^archieve/$', ArchieveFeed(), name='archieve-feed')

)

