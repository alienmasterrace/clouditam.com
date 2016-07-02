"""mysite URL Configuration

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
from django.conf.urls import include, url, patterns
from django.conf.urls.static import static
from django.contrib import admin
from django.views.generic import TemplateView

from app import settings

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('web.urls')),
    url(r'^dashboard/', include('dashboard.urls')),
    url('^social/', include('social.apps.django_app.urls', namespace='social')),
    url(r'^api/v1/', include('api.urls')),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += patterns('',
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.MAINTENANCE:
    urlpatterns = [
    url(r'^', TemplateView.as_view(template_name='web/maintenance.html')),
]