"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import url

from sermon.views import *

urlpatterns = [

    # Example: /
    url(r'^$', SermonTypeLV.as_view(), name='index'),

    # Example: /album/, same as /
    url(r'^sermon_type/$', SermonTypeLV.as_view(), name='sermon_type_list'),

    # Example: /album/99/
    url(r'^sermon_type/(?P<pk>\d+)/$', SermonTypeDV.as_view(), name='sermon_type_detail'),

    # Example: /photo/99/
    url(r'^content/(?P<pk>\d+)/$', ContentDV.as_view(), name='content_detail'),

    # Example: /album/add/
    url(r'^sermon_type/add/$',
        SermonTypeCV.as_view(), name="sermon_type_add",
    ),

    # Example: /album/change/
    url(r'^sermon_type/change/$',
        SermonTypeChangeLV.as_view(), name="sermon_type_change",
    ),

    # Example: /album/99/update/
    url(r'^sermon_type/(?P<pk>[0-9]+)/update/$',
        SermonTypeUV.as_view(), name="sermon_type_update",
    ),

    # Example: /album/99/delete/
    url(r'^sermon_type/(?P<pk>[0-9]+)/delete/$',
        SermonTypeDeleteView.as_view(), name="sermon_type_delete",
    ),

    # Example: /photo/add/
    url(r'^content/add/$',
        ContentCreateView.as_view(), name="content_add",
    ),

    # Example: /photo/change/
    url(r'^content/change/$',
        ContentChangeLV.as_view(), name="content_change",
    ),

    # Example: /photo/99/update/
    url(r'^content/(?P<pk>[0-9]+)/update/$',
        ContentUpdateView.as_view(), name="content_update",
    ),

    # Example: /photo/99/delete/
    url(r'^content/(?P<pk>[0-9]+)/delete/$',
        ContentDeleteView.as_view(), name="content_delete",
    ),
]

