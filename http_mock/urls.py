"""http_mock URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
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
from django.contrib import admin
from importlib import import_module
import utils.config as config
import json
import os

base_pkg = 'http_mock.views.'
base_func = 'execute'

urlpatterns = [
    url(r'^admin/', admin.site.urls),
]

urls = config.get_urls('http_mock/config/*[a-z0-9].py')

for u in urls:
    m = import_module(base_pkg+u['view'])
    v = getattr(m, base_func)
    urlpatterns.append(url(u['url'], v, {'response': u['response']}))
