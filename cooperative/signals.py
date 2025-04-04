from django.contrib.auth.models import User  # Import the User model
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from django.conf import settings
from .models import Membre
from django.contrib.auth.models import Group

@receiver(post_save, sender=Membre)
def notifier_administration(sender, instance, created, **kwargs):
    if created:
        # Envoyer un e-mail à l'administration
        sujet = f"Nouvelle demande d'adhésion - {instance.cooperative}"
        message = f"""
            Nouvelle demande d'adhésion reçue :
            Nom : {instance.nom}
            Prénom : {instance.prenom}
            Email : {instance.email}
            Cooperative choisie : {instance.cooperative}

            Connectez-vous à votre compte pour plus de détails.
            Cordialement,

        """
        send_mail(
            sujet,
            message,
            settings.DEFAULT_FROM_EMAIL,
            [settings.ADMIN_EMAIL],  # Remplacez par l'email de l'administrateur
        
            fail_silently=False,
        )
@receiver(post_save, sender=Membre)
def envoyer_identifiant(sender, instance, **kwargs):
    if instance.statusc == 'actif' and not instance.user:
        # Creation d'un compte utilisateur 
        username = f"{instance.numero_identification}"
        password = User.objects.make_random_password()

        user = User.objects.create_user(
            username=username,
            password=password,
            email=instance.email
        )
        #Assignation a un groupe
        groupe_membres = Group.objects.get(name='Membre')
        user.groups.add(groupe_membres)
        # Envoi des identifiants
        sujet = "Votre adhésion a été validée"
        message = f"""
            Bonjour {instance.prenom},
            
            Votre demande d'adhésion à {instance.cooperative} a été acceptée.
            
            Vos identifiants de connexion :
            Identifiant: {username}
            Mot de passe temporaire: {password}
            
            Connectez-vous ici : {settings.SITE_URL}/login
            """
        
        send_mail(
            sujet,
            message,
            settings.DEFAULT_FROM_EMAIL,
            [instance.email],
            fail_silently=False,
        )
        
        # Lier le compte utilisateur au membre
        instance.user = user
        instance.save(update_fields=['user'])
