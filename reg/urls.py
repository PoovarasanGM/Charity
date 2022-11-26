from django.urls import path,include
from . import views
urlpatterns = [
    path('', views.index,name='index'),
    path('register', views.regs,name='register'),
    path('code', views.code,name='code'),
    path('gallery', views.gallery,name='gallery'),
    path('blog', views.blog,name='blog'),
    path('about', views.about,name='about'),
    path('contact', views.contact,name='contact'),
    
]
