"""critique URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from . import views

app_name = 'reviews'

urlpatterns = [

    url(r'^register/$', views.register, name='register'),

    # left adding/editing movies to the django admin
    url(r'^movie/list/$', views.list_movies, name='list_movies'),
    url(r'^movie/list/page/(?P<page_id>[0-9]+)/$', views.list_movies, name='list_paged_movies'),
    url(r'^movie/(?P<pk>[0-9a-z-]+)/$', views.details_movie, name='details_movie'),

    url(r'^movie/(?P<pk>[0-9a-z-]+)/review/add/$', views.add_review, name='add_review'),

    # no review pk needs to be provided, as there is a one to one max
    url(r'^movie/(?P<pk>[0-9a-z-]+)/review/edit/$', views.edit_review, name='edit_review'),

    url(r'^.*/$', views.default_url_redirect, name='default_view'),
    url(r'^$', views.default_url_redirect, name='default_view'),





]
