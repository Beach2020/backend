from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^downvote/$', views.downvote, name='downvote'),
    url(r'^downvote-ext/$', views.downvote_ext, name='downvote_ext'),
]