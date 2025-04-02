from django import forms
from django.contrib.auth.models import User
from .models import Cooperative, Membre

# Formulaire pour l'inscription d'une Cooperative
class CooperativeForm(forms.ModelForm):
    class Meta:
        model = Cooperative
        fields = ['nom', 'adresse','numero_telephone', 'email_adresse', 'secteur_activite']
        widgets = {
            'nom': forms.TextInput(attrs={'class': 'form-control'}),
            'adresse': forms.TextInput(attrs={'class': 'form-control'}),
            'numero_telephone' : forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Numéro de téléphone'}),
            'email_adresse' : forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Adresse e-mail'}),
            'secteur_activite' : forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Secteur d\'activité'}),
        }
    # Nouvelle ligne ajouter pour verfier la saisie de mail
    email_adresse = forms.EmailField(
        label="Adresse email",
        required=True,
        error_messages={
            'invalid': "Veuillez entrer une adresse email valide.",
            'required': "Ce champ est obligatoire."
        }
    )


    #Ligne pour verifier si un mail existe deja ou pas 
    def verifier_mail(self):
        email_adresse = self.cleaned_data.get('email_adresse')
        if Cooperative.objects.filter(email_adresse=email_adresse).exists():
            raise("Cet adresse mail existe déjà")
        else:
            return email_adresse
        

# Formulaire de creation d'un membre

class MembreForm(forms.ModelForm):
    class Meta:
        model = Membre
        fields = ['nom', 'prenom', 'sexe', 'date_naissance', 'cooperative','adresse', 'numero_identification' ]
        widgets = {
            'nom': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'nom'}),  # Sélection de l'utilisateur
            'prenom': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Prénom'}),
            'sexe': forms.Select(attrs={'class': 'form-control'}),  # Choix (M/F)
            'date_naissance': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'cooperative': forms.Select(attrs={'class': 'form-control'}),  # Liste déroulante des coopératives
            'adresse': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Adresse'}),
            'numero_identification': forms.TextInput(attrs={'readonly': 'readonly'}),
        }

#Fromulaire de creation d'un administrateur
"""
class AdminRegistrationForm(UserCreationForm):
    class Meta:
        model = Administrateur
        fields = ['username', 'email', 'password1', 'password2', 'role']
        widgets = {
            'role': forms.Select(attrs={'class': 'form-control'}),
        }"""


# Formulaire d'inscription d'un membre
class InscriptionMembreForm(forms.ModelForm):
    cooperative = forms.ModelChoiceField(
        queryset=Cooperative.objects.all(),
        label="Choisissez votre coopérative",
        widget=forms.Select(attrs={'class': 'form-select'})
    )
    
    class Meta:
        model = Membre
        fields = ['nom', 'prenom', 'email_adresse', 'password', 'sexe', 'date_naissance', 'adresse', 'cooperative']
        widgets = {
            'date_naissance': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
        }