
from django.conf.urls import include, url
from django.contrib import admin
from rest_framework.urlpatterns import format_suffix_patterns
from city import views


urlpatterns = [
   url(r'^city/$', views.city_list),
    url(r'^city/(?P<pk>[0-9]+)$', views.city_detail),
]

urlpatterns = format_suffix_patterns(urlpatterns)