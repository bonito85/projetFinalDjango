from django.urls import path
from . import views


urlpatterns = [
    # chemin d'index (page principale)
    path('', views.index, name='index'),
    # path des inscriptions
    path('Inscriptions/cooperative_inscription/', views.cooperative_inscription, name='cooperative_inscription'),
    path('Inscriptions/membre_inscription/', views.inscrire_membre, name='inscrire_membre'),
    path('Inscriptions/visite/', views.visite, name='visite'),
    #path pour lister les elements 
    path('listes/listes_membres', views.liste_membre, name='liste_membre'),
    path('listes/listes_cooperative', views.liste_cooperative, name='listes_cooperative'),
    # path pour les details de la cooperatives
    path('details/details_cooperative/<int:id>', views.details_cooperative, name='details_cooperative'),
    # lien de details d'un membre 
    path('details/details_membre/<int:id>', views.details_membre, name='details_membre'),    
    
    #Inscription de membres
    path('Inscriptions/register/', views.register, name='register'),

    #suppression des membres
    path('membre/<int:membre_id>/supprimer/', views.supprimer_membre, name='supprimer_membre'),
    #suppression des cooperatives   
    path('cooperative/<int:cooperative_id>/supprimer/', views.supprimer_cooperative, name='supprimer_cooperative'),
    # Modification des membres
    path('modifier-membre/<int:membre_id>/',views.modifier_membre, name='modifier_membre'),
    # Modification des cooperatives
    path('modifier-cooperative/<int:cooperative_id>/', views.modifier_cooperative, name='modifier_cooperative'),
    # Lien de confirmation d'inscription de l'utilisateur
    path('Inscriptions/confirmation-insctiption/', views.confirmation_inscription, name='confirmation-inscription'),
]

