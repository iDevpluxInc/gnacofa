from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    
    path('about/', views.about, name='about'),

    path('management/', views.management, name='our-managment'),

    path('structure/', views.structure, name='our-structure'),

    path('archieve/', views.archieves, name='archieves'),

    path('project/', views.projects, name='projects'),

    path('news/', views.news, name='news'),

    path('events/', views.events, name='events'),

    path('photos/', views.photos, name='photos'),

    path('contact/', views.contact, name='contact-us'),

    path('faqs/', views.faqs, name='faqs'),

    path('covid/', views.covid, name='covid-update'),
]