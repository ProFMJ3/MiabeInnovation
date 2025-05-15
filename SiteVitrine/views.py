from django.shortcuts import render, redirect

from django.contrib import messages
from django.core.files.storage import FileSystemStorage
from django.utils import timezone

from .forms import PartnershipForm
from .models import PartnershipRequest  # Si vous voulez quand même sauvegarder en base

from .models import Temoignage
from .forms import ContactForm
from .models import ContactMessage

# Create your views here.

def home(request):

    return render(request, 'index.html')



def quiSommesNous(request):
    return render(request, 'pages/quiSommesNous.html')




def quiSommeNous(request):
    return render(request, 'pages/quiSommeNous.html')


    return render(request, 'index.html', {'active_page': 'accueil'})

def quiSommesNous(request):
    return render(request, 'pages/quiSommesNous.html')




def equipe(request):
    return render(request, 'pages/equipe.html')



def services(request):
    return render(request, 'pages/services.html')

def service(request):
    return render(request, 'pages/service.html')


def temoignages(request):
    return render(request, 'pages/temoignages.html')




def entreeContact(request):
    return render(request, 'pages/entreeContact.html')


def devenirPartenaire(request):
    return render(request, 'pages/devenirPartenaire.html')

def contact(request):
    return render(request, 'pages/contact.html')




def faqs(request):
    return render(request, 'pages/faqs.html')


def blog (request):
    return render(request, 'pages/blog.html')


def services(request):
    return render(request, 'pages/services.html')


def temoignages(request):
    return render(request, 'pages/temoignages.html', {'active_page': 'temoignages'})


def entreeContact(request):
    return render(request, 'pages/entreeContact.html', {'active_page': 'entreeContact'})


def devenirPartenaire(request):
    return render(request, 'pages/devenirPartenaire.html', {'active_page': 'devenirPartenaire'})	


def faqs(request):
    return render(request, 'pages/faqs.html', {'active_page': 'faqs'})



# SERVICES VIEWS

def devApplication(request):
    return render(request, 'pages/devApplication.html')

def webDesignMultimedia(request):
    return render(request, 'pages/webDesignMultimedia.html')

def communityManagement(request):
    return render(request, 'pages/communityManagement.html')

def maintenance(request):
    return render(request, 'pages/maintenance.html')

def automatisationIa(request):
    return render(request, 'pages/automatisationIa.html')

def automatisationTache(request):
    return render(request, 'pages/automatisationTache.html')




def sauvegardeTemoignage(request):
    if request.method == 'POST':
        nom_complet = request.POST.get('nom_complet')
        email = request.POST.get('email')
        profession = request.POST.get('profession')
        profile_photo = request.FILES.get('profile_photo')
        note = request.POST.get('note')
        contenu = request.POST.get('contenu')
        media = request.FILES.get('media')
        consentement_publication = request.POST.get('consentement_publication') == 'on'
        # Créer une instance de Temoignage
        temoignage = Temoignage(
            nom_complet=nom_complet,
            email=email,
            profession=profession,
            profile_photo=profile_photo,
            note=note,
            contenu=contenu,
            media=media,
            consentement_publication=consentement_publication
        )
        # Enregistrer le témoignage
        temoignage.save()
        # Rediriger vers la page de remerciement ou une autre page
        return redirect('temoignages')
    else:
        # Si la méthode n'est pas POST, afficher le formulaire
        return render(request, 'pages/temoignages.html')
    
        




def partnership_view(request):
    if request.method == 'POST':
        form = PartnershipForm(request.POST)
        if form.is_valid():
            # Création manuelle de l'objet si vous voulez sauvegarder
            PartnershipRequest.objects.create(
                company_name=form.cleaned_data['company_name'],
                contact_person=form.cleaned_data['contact_person'],
                company_email=form.cleaned_data['company_email'],
                company_phone=form.cleaned_data['company_phone'],
                partnership_type=form.cleaned_data['partnership_type'],
                collaboration_ideas=form.cleaned_data['collaboration_ideas']
            )
            
            messages.success(
                request,
                "Votre demande de partenariat a été envoyée avec succès. "
                "Notre équipe vous contactera dans les 24 heures."
            )
            return redirect('success')
    else:
        form = PartnershipForm()
    
    return render(request, 'pages/devenirPartenaire.html', {'form': form})

def partnership_success_view(request):
    return render(request, 'gestionFormulaire/partnership_success.html')






def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Création manuelle de l'objet ContactMessage
            ContactMessage.objects.create(
                nom=form.cleaned_data['nom'],
                prenom=form.cleaned_data['prenom'],
                email=form.cleaned_data['email'],
                telephone=form.cleaned_data['telephone'],
                sujet=form.cleaned_data['sujet'],
                message=form.cleaned_data['message']
            )
            
            messages.success(request, 'Votre message a été envoyé avec succès!')
            return redirect('contact')
    else:
        form = ContactForm()
    
    return render(request, 'pages/entreecontact.html', {'form': form})