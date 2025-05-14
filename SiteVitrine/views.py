from django.shortcuts import render, redirect

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



