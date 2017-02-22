from django.conf.urls import url
from Token import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    url(r'^tokens/$',views.TokenList.as_view()),
    url(r'^tokenspost/$',views.TokenPost.as_view()),
    url(r'^tokens/(?P<pk>[0-9]+)/$', views.TokenDetail.as_view()),
]
urlpatterns = format_suffix_patterns(urlpatterns)