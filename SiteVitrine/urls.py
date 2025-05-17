
from django.urls import path
from . import views
from SiteVitrine import  views



urlpatterns = [
    # URLS DE BASE
    path("", views.home, name="accueil"),
    path('quiSommesNous/', views.quiSommesNous, name='qui_sommes_nous'),
    path('equipe/', views.equipe, name='equipe'),
    path('blog/', views.blog, name='blog'),
   
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
>>>>>>> 9a68b9f1a9803d0eb386c315b426b53b50ecb377


<<<<<<< HEAD
    path('contact/', views.contact_view, name='contact'),
=======
    path('partnership_success/', views.partnership_success_view, name='partnership_success'),

>>>>>>> 9a68b9f1a9803d0eb386c315b426b53b50ecb377


]

