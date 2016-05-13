"""Clase5 URL Configuration

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
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from .views import IndexView, HomeView, GreetView, JsonView, ColorView, ColorsView, AddColor
from django.views.decorators.csrf import csrf_exempt
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'colors', views.ColorViewSet)


urlpatterns = [
    #url(r'^index/$', IndexView.as_view()),
    url(r'^$', csrf_exempt(IndexView.as_view())),
    url(r'^greet/([a-z]+)$', csrf_exempt(GreetView.as_view())),
    url(r'^json/$', csrf_exempt(JsonView.as_view())),
    url(r'^color/([a-z]+)/$', csrf_exempt(ColorView.as_view())),
    url(r'^colors/$', csrf_exempt(ColorsView.as_view())),
    url(r'^addcolors/$', csrf_exempt(AddColor.as_view())),
    url(r'^display/$', views.DisplayColors.as_view()),
]
