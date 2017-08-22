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
from notice.views import *

urlpatterns = [

    # Example: /
    url(r'^$', NoticeLV.as_view(), name='index'),

    # Example: /notice/ (same as /)
    url(r'^notice/$', NoticeLV.as_view(), name='notice_list'),

    # Example: /notice/django-example/
    url(r'^notice/(?P<slug>[-\w]+)/$', NoticeDV.as_view(), name='notice_detail'),

    # Example: /archive/
    url(r'^archive/$', NoticeAV.as_view(), name='notice_archive'),

    # Example: /2012/
    url(r'^(?P<year>\d{4})/$', NoticeYAV.as_view(), name='notice_year_archive'),

    # Example: /2012/nov/
    url(r'^(?P<year>\d{4})/(?P<month>[a-z]{3})/$', NoticeMAV.as_view(), name='notice_month_archive'),

    # Example: /2012/nov/10/
    url(r'^(?P<year>\d{4})/(?P<month>[a-z]{3})/(?P<day>\d{1,2})/$', NoticeDAV.as_view(), name='notice_day_archive'),

    # Example: /today/
    url(r'^today/$', NoticeTAV.as_view(), name='notice_today_archive'),

    # Example: /tag/
    url(r'^tag/$', TagTV.as_view(), name='tag_cloud'),  

    # Example: /tag/tagname/
    url(r'^tag/(?P<tag>[^/]+(?u))/$', NoticeTOL.as_view(), name='tagged_object_list'),

    # Example: /search/
    url (r'^search/$', SearchFormView.as_view(), name='search'),

    # Example: /bssearch/ (Bootstrap Search)
    url (r'^bssearch/$', BstrapSearchLV.as_view(), name='bssearch'),

    # Example: /add/
    url(r'^add/$',
        NoticeCreateView.as_view(), name="add",
    ),

    # Example: /change/
    url(r'^change/$',
        NoticeChangeLV.as_view(), name="change",
    ),

    # Example: /99/update/
    url(r'^(?P<pk>[0-9]+)/update/$',
        NoticeUpdateView.as_view(), name="update",
    ),

    # Example: /99/delete/
    url(r'^(?P<pk>[0-9]+)/delete/$',
        NoticeDeleteView.as_view(), name="delete",
    ),
]
