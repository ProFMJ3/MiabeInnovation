# from django.shortcuts import render, redirect

# from django.contrib import messages
# from django.core.files.storage import FileSystemStorage
# from django.utils import timezone

# from .models import PartnershipRequest  # Si vous voulez quand même sauvegarder en base

# from .models import Temoignage

# from .models import ContactMessage
# from django.shortcuts import render, redirect
# from django.contrib import messages



# # Create your views here.
# def home(request):

#     return render(request, 'index.html', {'active_page': 'accueil'})

# def quiSommesNous(request):
#     return render(request, 'pages/quiSommesNous.html')



# def equipe(request):
#     return render(request, 'pages/equipe.html')


# #def temoignages(request):
#     #return render(request, 'pages/temoignages.html')




# def entreeContact(request):
#     return render(request, 'pages/entreeContact.html')



# #def faqs(request):
#     #return render(request, 'pages/faqs.html')


# def blog (request):
#     return render(request, 'pages/blog.html')

# def temoignages(request):
#     return render(request, 'pages/temoignages.html', {'active_page': 'temoignages'})


# def faqs(request):
#     return render(request, 'pages/faqs.html', {'active_page': 'faqs'})


# # SERVICES VIEWS
# def devApplication(request):
#     return render(request, 'pages/devApplication.html')

# def webDesignMultimedia(request):
#     return render(request, 'pages/webDesignMultimedia.html')

# def communityManagement(request):
#     return render(request, 'pages/communityManagement.html')

# def maintenance(request):
#     return render(request, 'pages/maintenance.html')

# def automatisationIa(request):
#     return render(request, 'pages/automatisationIa.html')

# def automatisationTache(request):
#     return render(request, 'pages/automatisationTache.html')


# def sauvegardeTemoignage(request):
#     if request.method == 'POST':
#         nom_complet = request.POST.get('nom_complet')
#         email = request.POST.get('email')
#         profession = request.POST.get('profession')
#         profile_photo = request.FILES.get('profile_photo')
#         note = request.POST.get('note')
#         contenu = request.POST.get('contenu')
#         media = request.FILES.get('media')
#         consentement_publication = request.POST.get('consentement_publication') == 'on'
#         # Créer une instance de Temoignage
#         temoignage = Temoignage(
#             nom_complet=nom_complet,
#             email=email,
#             profession=profession,
#             profile_photo=profile_photo,
#             note=note,
#             contenu=contenu,
#             media=media,
#             consentement_publication=consentement_publication
#         )
#         # Enregistrer le témoignage
#         temoignage.save()
#         # Rediriger vers la page de remerciement ou une autre page
#         messages.success(request, "Votre témoignage a été envoyée avec succès. Nous analysons pour la publier ")

#         return redirect('temoignages')
#     else:
#         # Si la méthode n'est pas POST, afficher le formulaire
#         return render(request, 'pages/temoignages.html')
    


# def devenirPartenaire(request):
#     if request.method == 'POST':
#         # Récupération des données manuellement
#         company_name = request.POST.get('company_name')
#         contact_person = request.POST.get('contact_person')
#         company_email = request.POST.get('company_email')
#         company_phone = request.POST.get('company_phone')
#         partnership_type = request.POST.get('partnership_type')
#         collaboration_ideas = request.POST.get('collaboration_ideas')

#         # Validation manuelle
#         errors = []
#         if not company_name:
#             errors.append("Le nom de l'entreprise est requis")
#         if not contact_person:
#             errors.append("La personne de contact est requise")
#         if not company_email:
#             errors.append("L'email professionnel est requis")
#         elif '@' not in company_email:
#             errors.append("Veuillez entrer un email valide")
#         if not partnership_type:
#             errors.append("Veuillez sélectionner un type de partenariat")
#         if not collaboration_ideas:
#             errors.append("Veuillez décrire vos idées de collaboration")

#         if not errors:
#             # Création de la demande de partenariat
#             PartnershipRequest.objects.create(
#                 company_name=company_name,
#                 contact_person=contact_person,
#                 company_email=company_email,
#                 company_phone=company_phone,
#                 partnership_type=partnership_type,
#                 collaboration_ideas=collaboration_ideas
#             )
#             messages.success(request, "Votre demande a été envoyée avec succès. Nous vous contacterons dans les 24h.")
#             return redirect('partnership_success')
#         else:   
#             for error in errors:
#                 messages.error(request, error)

#     # Préparation des données pour le template
   

#     context = {
#         'submitted_data': {
#             'company_name': request.POST.get('company_name', ''),
#             'contact_person': request.POST.get('contact_person', ''),
#             'company_email': request.POST.get('company_email', ''),
#             'company_phone': request.POST.get('company_phone', ''),
#             'partnership_type': request.POST.get('partnership_type', ''),
#             'collaboration_ideas': request.POST.get('collaboration_ideas', ''),
#         },
#         'partnership_types': PartnershipRequest.PARTNERSHIP_TYPES,
#         'active_tab': 'partnership'
#     }
#     return render(request, 'pages/devenirPartenaire.html', context)

# def partnership_success(request):
#     return render(request, 'gestionFormulaire/partnership_success.html', {
#         'title': 'Demande envoyée'
#     })

# # Contact form view

# def entreeContact(request):
#     if request.method == 'POST':
#         # Récupération des données du formulaire
#         nom = request.POST.get('nom')
#         prenom = request.POST.get('prenom')
#         email = request.POST.get('email')
#         telephone = request.POST.get('telephone')
#         sujet = request.POST.get('sujet')
#         message = request.POST.get('message')

#         # Validation de base
#         errors = []
#         if not nom:
#             errors.append("Le nom est obligatoire")
#         if not email:
#             errors.append("L'email est obligatoire")
#         if not message:
#             errors.append("Le message est obligatoire")

#         if not errors:
#             # Création et sauvegarde du message
#             ContactMessage.objects.create(
#                 nom=nom,
#                 prenom=prenom,
#                 email=email,
#                 telephone=telephone,
#                 sujet=sujet,
#                 message=message
#             )
#             messages.success(request, 'Votre message a été envoyé avec succès!')
#             return redirect('entree_contact')
#         else:
#             for error in errors:
#                 messages.error(request, error)

#     # Contexte avec les valeurs soumises pour ré-affichage
#     context = {
#         'submitted_data': {
#             'nom': request.POST.get('nom', ''),
#             'prenom': request.POST.get('prenom', ''),
#             'email': request.POST.get('email', ''),
#             'telephone': request.POST.get('telephone', ''),
#             'sujet': request.POST.get('sujet', ''),
#             'message': request.POST.get('message', ''),
#         },
#         'active_page': 'entreeContact',
#         'sujet_choices': ContactMessage.SUJET_CHOICES
#     }
#     return render(request, 'pages/entreecontact.html', context)


from django.shortcuts import render, redirect

from django.contrib import messages

from .models import Temoignage, ContactMessage ,  PartnershipRequest



# Create your views here.
def home(request):


    return render(request, 'index.html', {'active_page': 'accueil'})

def quiSommesNous(request):
    return render(request, 'pages/quiSommesNous.html')



def equipe(request):
    return render(request, 'pages/equipe.html')


#def temoignages(request):
    #return render(request, 'pages/temoignages.html')




# def entreeContact(request):
#     return render(request, 'pages/entreeContact.html')



#def faqs(request):
    #return render(request, 'pages/faqs.html')


def blog (request):
    return render(request, 'pages/blog.html')

def temoignages(request):
    return render(request, 'pages/temoignages.html', {'active_page': 'temoignages'})


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
        messages.success(request, "Votre témoignage a été envoyée avec succès. Nous analysons pour la publier ")

        return redirect('temoignages')
    else:
        # Si la méthode n'est pas POST, afficher le formulaire
        return render(request, 'pages/temoignages.html')



def devenirPartenaire(request):
    if request.method == 'POST':
        # Récupération des données manuellement
        company_name = request.POST.get('company_name')
        contact_person = request.POST.get('contact_person')
        company_email = request.POST.get('company_email')
        company_phone = request.POST.get('company_phone')
        partnership_type = request.POST.get('partnership_type')
        collaboration_ideas = request.POST.get('collaboration_ideas')

        # Validation manuelle
        errors = []
        if not company_name:
            errors.append("Le nom de l'entreprise est requis")
        if not contact_person:
            errors.append("La personne de contact est requise")
        if not company_email:
            errors.append("L'email professionnel est requis")
        elif '@' not in company_email:
            errors.append("Veuillez entrer un email valide")
        if not partnership_type:
            errors.append("Veuillez sélectionner un type de partenariat")
        if not collaboration_ideas:
            errors.append("Veuillez décrire vos idées de collaboration")

        if not errors:
            # Création de la demande de partenariat
            PartnershipRequest.objects.create(
                company_name=company_name,
                contact_person=contact_person,
                company_email=company_email,
                company_phone=company_phone,
                partnership_type=partnership_type,
                collaboration_ideas=collaboration_ideas
            )
            messages.success(request, "Votre demande a été envoyée avec succès. Nous vous contacterons dans les 24h.")
            return redirect('partnership_success')
        else:
            for error in errors:
                messages.error(request, error)

    # Préparation des données pour le template


    context = {
        'submitted_data': {
            'company_name': request.POST.get('company_name', ''),
            'contact_person': request.POST.get('contact_person', ''),
            'company_email': request.POST.get('company_email', ''),
            'company_phone': request.POST.get('company_phone', ''),
            'partnership_type': request.POST.get('partnership_type', ''),
            'collaboration_ideas': request.POST.get('collaboration_ideas', ''),
        },
        'partnership_types': PartnershipRequest.PARTNERSHIP_TYPES,
        'active_tab': 'partnership'
    }
    return render(request, 'pages/devenirPartenaire.html', context)

def partnership_success(request):
    return render(request, 'gestionFormulaire/partnership_success.html', {
        'title': 'Demande envoyée'
    })

# Contact form view

def entreeContact(request):
    if request.method == 'POST':
        # Récupération des données du formulaire
        nom = request.POST.get('nom')
        prenom = request.POST.get('prenom')
        email = request.POST.get('email')
        telephone = request.POST.get('telephone')
        sujet = request.POST.get('sujet')
        message = request.POST.get('message')

        # Validation de base
        errors = []
        if not nom:
            errors.append("Le nom est obligatoire")
        if not email:
            errors.append("L'email est obligatoire")
        if not message:
            errors.append("Le message est obligatoire")

        if not errors:
            # Création et sauvegarde du message
            ContactMessage.objects.create(
                nom=nom,
                prenom=prenom,
                email=email,
                telephone=telephone,
                sujet=sujet,
                message=message
            )
            messages.success(request, 'Votre message a été envoyé avec succès!')
            return redirect('entree_contact')
        else:
            for error in errors:
                messages.error(request, error)

    # Contexte avec les valeurs soumises pour ré-affichage
    context = {
        'submitted_data': {
            'nom': request.POST.get('nom', ''),
            'prenom': request.POST.get('prenom', ''),
            'email': request.POST.get('email', ''),
            'telephone': request.POST.get('telephone', ''),
            'sujet': request.POST.get('sujet', ''),
            'message': request.POST.get('message', ''),
        },
        'active_page': 'entreeContact',
        'sujet_choices': ContactMessage.SUJET_CHOICES
    }
    return render(request, 'pages/entreeContact.html', context)