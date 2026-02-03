
from  django.shortcuts import render

from django.http import HttpResponse

from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.contrib import messages
from django.views.decorators.http import require_http_methods

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

#def contacts(request):
   # return render(request, 'contacts.html') 


def contacts(request):
    if request.method == 'POST':
        nom = request.POST.get('nom')
        email = request.POST.get('email')
        specialite = request.POST.get('specialite')
        message_text = request.POST.get('message')
        
        try:
            # Email à l'hôpital
            send_mail(
                subject=f"Nouveau message de {nom} - {specialite}",
                message=f"Nom: {nom}\nEmail: {email}\nSpécialité: {specialite}\n\nMessage:\n{message_text}",
                from_email='hopitalmariewyss544@gmail.com',
                recipient_list=['hopitalmariewyss544@gmail.com'],
                fail_silently=False,
            )
            
            # Email de confirmation au client
            send_mail(
                subject="Confirmation de votre message",
                message=f"Bonjour {nom},\n\nMerci d'avoir contacté l'Hôpital Marie Wyss. Nous avons reçu votre message et vous répondrons dans les plus brefs délais.\n\nCordialement,\nL'équipe de l'Hôpital Marie Wyss",
                from_email='hopitalmariewyss544@gmail.com',
                recipient_list=[email],
                fail_silently=False,
            )
            
            messages.success(request, '✓ Votre message a été envoyé avec succès!')
            return redirect('contacts')
            
        except Exception as e:
            messages.error(request, f'✗ Erreur: {str(e)}')
            return redirect('contacts')
    
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



