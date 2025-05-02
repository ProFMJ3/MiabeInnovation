from django.shortcuts import render, redirect

# Create your views here.

def home(request):
    return render(request, 'index.html')

def quiSommesNous(request):
    return render(request, 'pages/quiSommesNous.html')


def equipe(request):
    return render(request, 'pages/equipe.html')


def services(request):
    return render(request, 'pages/services.html')


def temoignages(request):
    return render(request, 'pages/temoignages.html')


def entreeContact(request):
    return render(request, 'pages/entreeContact.html')


def devenirPartenaire(request):
    return render(request, 'pages/devenirPartenaire.html')


def faqs(request):
    return render(request, 'pages/faqs.html')