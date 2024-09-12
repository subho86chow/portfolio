from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name='home'),
    path('portfolio/',views.portfolio, name='portfolio'),
    path('portfolio/<str:str>/',views.project_details, name='portfolio'),
    path('services/',views.services, name='services'),
    path('web-dev/',views.webdev, name='webdev'),
    # path('advertisement-marketing/',views.marketing, name='marketing'),
    # path('graphics-brand-designing/',views.designing, name='designing'),
    path('custom-development/',views.customdev, name='customdev'),
    path('contact/',views.contact, name='contact'),
    path('twitter/', views.facebook, name='twitter'),
    path('instagram/', views.instagram, name='instagram'),
    path('linkedin/', views.linkedin, name='linkedin'),
    path('calendely/', views.calendely, name='calendely'),
]