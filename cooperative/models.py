from django.db import models
from django.contrib.auth.models import User
import random
import string
from django.utils.timezone import now
from django.contrib.auth.models import AbstractUser


#Ajout de la classe Cooperative
class Cooperative(models.Model):
    nom = models.CharField(max_length=255)
    adresse = models.TextField(max_length=150, null=True, blank=True)
    numero_telephone = models.CharField(max_length=15, verbose_name="Téléphone", blank=True, null=True)
    email_adresse = models.EmailField(verbose_name="Email", blank=True, null=True)
    secteur_activite = models.CharField(max_length=255, verbose_name="Secteur d'activité", null=True)
    date_creation = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.nom} - {self.secteur_activite}"
    class Meta:
        verbose_name = "Coopérative"
        verbose_name_plural = "Coopératives"
        ordering = ['nom']
""""
# Classe permettant de creer un administrateur
class Administrateur(AbstractUser):
    # Choix des rôles
    CHOICES_ROLES = [
        ('super_admin', 'Super Administrateur'),
        ('admin', 'Administrateur'),
    ]
    role = models.CharField(max_length=20, choices=CHOICES_ROLES, default='admin')

    # Corriger les conflits en ajoutant des related_name uniques
    groups = models.ManyToManyField(Group, related_name="administrateurs_groups", blank=True)
    user_permissions = models.ManyToManyField(Permission, related_name="administrateurs_permissions", blank=True)

    # Méthodes pour vérifier le rôle
    def is_super_admin(self):
        return self.role == 'super_admin'

    def is_admin(self):
        return self.role == 'admin'

"""


class Membre(models.Model):
    SEXE_CHOICES = [
        ('M', 'Masculin'),
        ('F', 'Féminin'),
    ]
    
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True) 
    nom = models.CharField(max_length=255, null=True, blank=True)
    prenom = models.CharField(max_length=150, null=True, blank=True)
    sexe = models.CharField(max_length=1, choices=SEXE_CHOICES, default="M")
    date_naissance = models.DateField(null=True, blank=True)
    cooperative = models.ForeignKey(Cooperative, related_name='membres', on_delete=models.CASCADE, null=True)  # Assure-toi qu'il est défini pour accepter des valeurs null
    adresse = models.CharField(max_length=255)
    numero_identification = models.CharField(max_length=6, unique=True)  # Exemple : "ABC123"
    # Ajout du statut choices de l'utilisateur
    date_inscription = models.DateField(auto_now_add=True)
    # Ajout d'un champ de téléphone
    #numero_telephone = models.CharField(max_length=15, verbose_name="Téléphone", blank=True, null=True)
    # Ajout d'un champ d'email
    email_adresse = models.EmailField(verbose_name="Email", blank=True, null=True)
    # Ajout d'un mot de passe 
    password = models.CharField(max_length=255, null=True, blank=True)


    def save(self, *args, **kwargs):
        if not self.numero_identification:  # Générer uniquement si vide
            self.numero_identification = self.generate_identification()
        super().save(*args, **kwargs)

    def generate_identification(self):
        lettres = ''.join(random.choices(string.ascii_uppercase, k=3))  # 3 lettres majuscules
        chiffres = ''.join(random.choices(string.digits, k=3))  # 3 chiffres
        return f"{lettres}{chiffres}"  # Exemple : "XYZ987"

    def __str__(self):
        return f"{self.nom}"
    
    class Meta:
        ordering = ['-date_inscription']


"""

class Membre(AbstractUser):
    SEXE_CHOICES = [
        ('M', 'Masculin'),
        ('F', 'Féminin'),
    ]

    # Champs hérités d'AbstractUser (à personnaliser)
    nom = models.CharField("prénom", max_length=150, null=True, blank=True)
    prenom = models.CharField("nom", max_length=255, null=True, blank=True)
    email_adresse = models.EmailField("email", blank=True, null=True)

    # Nouveaux champs spécifiques
    sexe = models.CharField(max_length=1, choices=SEXE_CHOICES, default="M")
    date_naissance = models.DateField(null=True, blank=True)
    cooperative = models.ForeignKey('Cooperative', related_name='membres', on_delete=models.CASCADE, null=True)
    adresse = models.CharField(max_length=255)
    numero_identification = models.CharField(max_length=6, unique=True)
    date_inscription = models.DateField(auto_now_add=True)

    # Désactiver les champs inutiles d'AbstractUser
    username = models.CharField(
        max_length=150,
        unique=True,
        null=True,
        blank=True,
        help_text="Non requis"
    )

    def save(self, *args, **kwargs):
        if not self.numero_identification:
            self.numero_identification = self.generate_identification()
        super().save(*args, **kwargs)

    def generate_identification(self):
        lettres = ''.join(random.choices(string.ascii_uppercase, k=3))
        chiffres = ''.join(random.choices(string.digits, k=3))
        return f"{lettres}{chiffres}"

    class Meta(AbstractUser.Meta):
        ordering = ['-date_inscription']
        verbose_name = "Membre"
        verbose_name_plural = "Membres"

    def __str__(self):
        return f"{self.last_name}"



"""
