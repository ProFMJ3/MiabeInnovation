
from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="accueil"),
    path('quiSommesNous/', views.quiSommesNous, name='qui_sommes_nous'),
    path('equipe/', views.equipe, name='equipe'),
    path('services/', views.services, name='services'),
    path('temoignages/', views.temoignages, name='temoignages'),
    path('entreeContact/', views.entreeContact, name='entree_contact'),
    path('devenirPartenaire/', views.devenirPartenaire, name='devenir_partenaire'),
    path('faqs/', views.faqs, name='faqs')
]
