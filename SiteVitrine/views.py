from django.shortcuts import render, redirect

# Create your views here.

def home(request):
    return render(request, 'index.html')

<<<<<<< HEAD
def quiSommesNous(request):
    return render(request, 'pages/quiSommesNous.html')
=======

def quiSommeNous(request):
    return render(request, 'pages/quiSommeNous.html')
>>>>>>> a184f4b0c0e2adb34b323298c701548978c35c5b


def equipe(request):
    return render(request, 'pages/equipe.html')


<<<<<<< HEAD
def services(request):
    return render(request, 'pages/services.html')
=======
def service(request):
    return render(request, 'pages/service.html')
>>>>>>> a184f4b0c0e2adb34b323298c701548978c35c5b


def temoignages(request):
    return render(request, 'pages/temoignages.html')


<<<<<<< HEAD
def entreeContact(request):
    return render(request, 'pages/entreeContact.html')


def devenirPartenaire(request):
    return render(request, 'pages/devenirPartenaire.html')
=======
def contact(request):
    return render(request, 'pages/contact.html')


>>>>>>> a184f4b0c0e2adb34b323298c701548978c35c5b


def faqs(request):
    return render(request, 'pages/faqs.html')


<<<<<<< HEAD
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
=======









>>>>>>> a184f4b0c0e2adb34b323298c701548978c35c5b
