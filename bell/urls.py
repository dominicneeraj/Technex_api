from django.conf.urls import include, url
from django.contrib import admin
from rest_framework.urlpatterns import format_suffix_patterns
from bell import views


urlpatterns = [
     url(r'^city/$', views.CityList.as_view()),
   url(r'^city/(?P<pk>[0-9]+)/$', views.CityDetail.as_view()),

   url(r'^restra/$', views.RestraList.as_view()),
    url(r'^restra/(?P<pk>[0-9]+)$', views.RestraDetail.as_view()),

    url(r'^deal/$', views.DealList.as_view()),
    url(r'^deal/(?P<pk>[0-9]+)$', views.DealDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)