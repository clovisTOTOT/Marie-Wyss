
from  django.urls import path

from apps import views, admin

from .views import privacy_policy_view  # Assurez-vous d'importer la bonne vue

urlpatterns = [
    path('', views.home, name='accueil'),
    path('services/', views.services, name='services'),
    path('apropos/', views.apropos, name='apropos'),
    path('galerie-image/', views.galerie_image, name='galerie_image'),
    path('actualite/', views.actualite, name='actualite'),
    path('teleconsultation/', views.teleconsultation, name='teleconsultation'),
    path('contacts/', views.contacts, name='contacts'),
     path('Docteur1/', views.docteur1_view, name='docteur1'),
    path('Docteur2/', views.docteur2_view, name='docteur2'),
    path('Docteur3/', views.docteur3_view, name='docteur3'),
    path('Docteur4/', views.docteur4_view, name='docteur4'),
    path('notre-equipe/', views.notreequipe_view, name='notre_equipe'),
    path('book-appointment/', views.book_appointment, name='book_appointment'),
     path('privacy-policy/', privacy_policy_view, name='privacy_policy'),

]





