
from django.urls import path
<<<<<<< HEAD
from . import views

urlpatterns = [
    path("", views.home, name="accueil"),
    path('quiSommesNous/', views.quiSommesNous, name='qui_sommes_nous'),
    path('equipe/', views.equipe, name='equipe'),
    path('services/', views.services, name='services'),
    path('temoignages/', views.temoignages, name='temoignages'),
    path('entreeContact/', views.entreeContact, name='entree_contact'),
    path('devenirPartenaire/', views.devenirPartenaire, name='devenir_partenaire'),
    path('faqs/', views.faqs, name='faqs'),

    # SERVICES URLS

    path("developpment-d'application", views.devApplication, name="devApplication"),
    path("web-design-et-multimedia", views.webDesignMultimedia, name="webDesignMultimedia"),
    path("automatisation-avec-ia", views.automatisationIa, name="automatisationIa"),
    path("automatisation-des-taches", views.automatisationTache, name="automatisationTache"),
    path("community-management", views.communityManagement, name="communityManagement"),
    path("maintenance-logiciels", views.maintenance, name="maintenance"),
=======
from SiteVitrine import  views

urlpatterns = [
    path('', views.home, name ='home'),
>>>>>>> a184f4b0c0e2adb34b323298c701548978c35c5b
]
