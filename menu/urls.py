
from django.conf.urls import include, url
from django.contrib import admin
from rest_framework.urlpatterns import format_suffix_patterns
from menu import views


urlpatterns = [
   url(r'^menu/$', views.menu_list),
    url(r'^menu/(?P<pk>[0-9]+)$', views.menu_detail),
]

urlpatterns = format_suffix_patterns(urlpatterns)