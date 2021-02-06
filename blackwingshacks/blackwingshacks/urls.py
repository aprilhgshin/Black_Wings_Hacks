"""blackwingshacks URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import url, include
from . import views

urlpatterns = [
    url('^admin/', admin.site.urls),
    url(r'^user_data', include('user_data.urls')), # now django knows to look into urls in app_1
    url(r'^about/$', views.about), #about url
    url(r'^$', views.homepage) # homepage url
]
