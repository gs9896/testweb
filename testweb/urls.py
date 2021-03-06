"""testweb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin

from . import view
from . import testdb
from . import getdb
from . import changedb
from . import deletedb
from . import search, search2
from wechat import views

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', view.hello),
    url(r'^testdb$', testdb.testdb),
    url(r'^getdb$', getdb.getdb),
    url(r'^changedb$', changedb.changedb),
    url(r'^deletedb$', deletedb.deletedb),
    url(r'^search$', search.search),
    url(r'^search-form$', search.search_form),
    url(r'^search-post$', search2.search_post),
    url(r'^wechat$', views.main),
]
