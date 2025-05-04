
from django.urls import path
from SiteVitrine import  views

urlpatterns = [
    path('', views.home, name ='home'),
]
