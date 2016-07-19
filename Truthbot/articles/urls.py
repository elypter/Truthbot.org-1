from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'article/(?P<url>.+)/$', views.article_view, name='article'),
    url(r'id/(?P<article_pk>\d+)/new-review/$', views.article_create_review, name='articlecreatereview'),
    url(r'review/(?P<review_pk>\d+)/$', views.article_review_view, name='articlereviewview'),
    url(r'review/(?P<review_pk>\d+)/edit/$', views.article_edit_review, name='articleeditreview'),
]