from django.conf.urls import include, url
from django.contrib import admin
from rest_framework.urlpatterns import format_suffix_patterns
from mining import views


urlpatterns = [
   url(r'^chapter/$', views.ChapterList.as_view()),
    url(r'^chapter/(?P<pk>[0-9]+)$', views.ChaptertDetail.as_view()),
    url(r'^subject/$', views.SubjectList.as_view()),
   url(r'^subject/(?P<pk>[0-9]+)/$', views.SubjectDetail.as_view()),
    url(r'^content/$', views.ContentList.as_view()),
    url(r'^content/(?P<pk>[0-9]+)$', views.ContentDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)