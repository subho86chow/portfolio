from django.urls import re_path as url
from django.views.static import serve
from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.sitemaps.views import sitemap
from website.sitemaps import *
from django.views.generic.base import TemplateView



sitemaps = {
    'static': StaticSitemap,
    'projects': ProjectsSitemap,
}


urlpatterns = [
    url(r'^media/(?P<path>.*)$', serve,{'document_root':settings.MEDIA_ROOT}),
    url(r'^static/(?P<path>.*)$', serve,{'document_root':settings.STATIC_ROOT}),
    path('sitemap.xml/',sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
    path('robots.txt/',TemplateView.as_view(template_name="robots.txt",content_type="text/plain")),
    path('admin/', admin.site.urls),
    path('captcha/', include('captcha.urls')),
    path('',include('website.urls')),
]
handler404 = 'website.views.handeling404'
urlpatterns += static( settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
urlpatterns += static( settings.STATIC_URL, document_root = settings.STATIC_ROOT)
