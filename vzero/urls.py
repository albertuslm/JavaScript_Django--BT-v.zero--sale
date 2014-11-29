from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^$', 'vzero.views.index', name='index'),
    url(r'^checkout', 'vzero.views.checkout', name='checkout'),

)
