"""tryTen URL Configuration

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
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from django.contrib import admin

from profiles import views as profiles_views
from contact import views as contact_views
from login.views import (login_view, register_view, logout_view, profile_edit) 

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', profiles_views.home, name='home'),
    url(r'^about/$', profiles_views.about, name='about'),
    url(r'^instellingen/$', profiles_views.instellingen, name='instellingen'),
    url(r'^voorkeurlijst/$', profiles_views.voorkeurlijst, name='voorkeurlijst'),
    url(r'^infolijst/$', profiles_views.infolijst, name='infolijst'),
    url(r'^contact/$', contact_views.contact, name='contact'),
    url(r'^login/$', login_view, name='login'),
    url(r'^logout/$', logout_view, name='logout'),
    url(r'^register/$', register_view, name='register'),
    url(r'^register/profile/$', profile_edit, name='profile'),
]
 
if settings.DEBUG:
 	urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) 
 	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 