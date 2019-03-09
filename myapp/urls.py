from django.conf.urls import url,path
from . import views

urlpatterns = [
    url(r'^downvote/$', views.downvote, name='downvote'),
    url(r'^downvote-ext/$', views.downvote_ext, name='downvote_ext'),
    path('d/<int:pid>/<str:uid>/', views.d, name='d'),
]