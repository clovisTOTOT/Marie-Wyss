"""
URL configuration for educ_proc project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from apps import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'),  # Ajoutez cette ligne pour la racine
    path('admin/', admin.site.urls),
    # Direct routes for docteurs (so links like /Docteur2/ work)
     path('whatsapp/', views.whatsapp, name='whatsapp'),
    path('Docteur1/', views.docteur1_view, name='docteur1'),
    path('Docteur2/', views.docteur2_view, name='docteur2'),
    path('Docteur3/', views.docteur3_view, name='docteur3'),
    path('Docteur4/', views.docteur4_view, name='docteur4'),
    path('notre-equipe/', views.notreequipe_view, name='notre_equipe'),
    path('apps/', include('apps.urls')),
    path('__reload__/', include('django_browser_reload.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
