from django.shortcuts import render, redirect

# Create your views here.

def home(request):
    return render(request, 'index.html')


def quiSommeNous(request):
    return render(request, 'pages/quiSommeNous.html')


def equipe(request):
    return render(request, 'pages/equipe.html')


def service(request):
    return render(request, 'pages/service.html')


def temoignages(request):
    return render(request, 'pages/temoignages.html')


def contact(request):
    return render(request, 'pages/contact.html')




def faqs(request):
    return render(request, 'pages/faqs.html')











