
from django.urls import path
from . import views
from SiteVitrine import  views



urlpatterns = [
    # URLS DE BASE
    path("", views.home, name="accueil"),
    path('quiSommesNous/', views.quiSommesNous, name='qui_sommes_nous'),
    path('equipe/', views.equipe, name='equipe'),
    path('blog/', views.blog, name='blog'),
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


    #URL DE SAUVEGARDE
    path('sauvegardeTemoignage/', views.sauvegardeTemoignage, name='sauvegardeTemoignage'),
<<<<<<< HEAD
=======

    path('partnership_form', views.partnership_view, name='partnership_form'),
    path('success/', views.partnership_success_view, name='success'),

    path('contact/', views.contact_view, name='contact'),
>>>>>>> ba22e6b31cc78bcf265e296347b4b0a42f79a452

]

