"""cockroach_example URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/

"""
from django.contrib import admin
from . import views
from django.conf.urls import url

urlpatterns = [
    url('admin/', admin.site.urls),
    url(r'^userPage/$', views.user_page), #user page url
    url(r'^about/$', views.about), #about url
    url(r'^$', views.homepage) # homepage url
]
