from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from .models import *


class StaticSitemap(Sitemap):
    def items(self):
        return ['home','portfolio','webdev','customdev','services','contact']
    
    def location(self,item):
        return reverse(item)
    
class ProjectsSitemap(Sitemap):
    def items(self):
        return Projects.objects.all()