
from  django.shortcuts import render

from django.http import HttpResponse


def home(request):

        return  render(request, 'index.html')


def services(request):
    return render(request, 'services.html')  

def actualite(request):
    return render(request, 'actualite.html')

def apropos(request):
    return render(request, 'apropos.html')

def galerie_image(request):
    return render(request, 'galerie-image.html') 

def teleconsultation(request):
    return render(request, 'teleconsultation.html') 

def contacts(request):
    return render(request, 'contacts.html') 

def whatsapp(request):
    return render(request, 'whatsapp.html')

def header(request):
    return render(request, 'header.html')

def footer(request):
    return render(request, 'footer.html')       

def docteur1_view(request):
    return render(request, 'Docteur1.html')

def docteur2_view(request):
    return render(request, 'Docteur2.html')

def docteur3_view(request):
    return render(request, 'Docteur3.html')

def docteur4_view(request):
    return render(request, 'Docteur4.html')

def book_appointment(request):
    if request.method == 'POST':
        # Traitez les données du formulaire ici
        pass
    return render(request, 'appointment.html')  # Remplacez par le bon template

def privacy_policy_view(request):
    return render(request, 'privacy_policy.html')  # Remplacez par le bon template   


def notreequipe_view(request):
    return render(request, 'notreequipe.html')



