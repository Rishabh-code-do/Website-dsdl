from django.urls import path

from . import views

urlpatterns =[
    path('',views.index,name='index'),
    path('teams',views.teams,name='teams'),
    path('about',views.about,name='about'),
    path('events',views.events,name='events'),
    path('blogs',views.blogs,name='blogs'),
    path('contact',views.contact,name='contact')
]
