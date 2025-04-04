from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.template import loader
from .forms import CooperativeForm, MembreForm, InscriptionMembreForm
from django.contrib import messages
from .models import Membre, Cooperative
from django.views.generic import DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


# Afficher les informations d'un membre dans la page de confirmation d'inscription
def confirmation_inscription(request, membre_id):
    membre = get_object_or_404(Membre, pk=membre_id)
    return render(request, 'Incription/confirmation_inscription.html', {'membre': membre})


def index(request): 
    template = loader.get_template('pages/index.html')
    return HttpResponse(template.render())



# Fonction permettant d'inscrire une cooperative 
def cooperative_inscription(request):
    if request.method == "POST":
        cooperative_form = CooperativeForm(request.POST)
        if cooperative_form.is_valid():
            cooperative_form.save()
            messages.success(request, "La coopérative est crée avec succès !")
            return redirect('accounts:dashboard')
    else:
        cooperative_form = CooperativeForm()
    return render(request, 'Inscriptions/cooperative_inscription.html', {'cooperative_form': cooperative_form})

# Fonction permettant d'inscrire un membre 
def inscrire_membre(request):
    if request.method == "POST":
        membre_form = MembreForm(request.POST)
        if membre_form.is_valid():
            membre_form.save()
            messages.success(request, "Membre ajouté avec succès !")
            return redirect('accounts:dashboard')
    else:
        membre_temp = Membre()
        membre_temp.numero_identification = membre_temp.generate_identification()
        membre_form = MembreForm(instance=membre_temp)
        #membre_form = MembreForm()
    return render(request, 'Inscriptions/membre_inscription.html', {'membre_form': membre_form})


# Vue permettant d'afficher les la visite sur les inscriptions des utilisateurs 

def visite(request):
    template = loader.get_template("Inscriptions/visite.html")
    return HttpResponse(template.render())


# Lister les membres 

def liste_membre(request):
    liste_membre = Membre.objects.select_related('cooperative').all()
    template  = loader.get_template('listes/listes_membres.html')
    context = {
        'liste_membre' : liste_membre,
    }
    return HttpResponse(template.render(context, request))

# Lister les cooperatives

def liste_cooperative(request): 
    liste_cooperative = Cooperative.objects.all().values()
    template = loader.get_template('listes/listes_cooperative.html')
    context = {
        'liste_cooperative' : liste_cooperative
    }
    return  HttpResponse(template.render(context, request))

# Lister les details de la cooperative

def details_cooperative(request, id): 
    details_cooperative = Cooperative.objects.get(id=id)
    template = loader.get_template('details/details_cooperative.html')
    context = {
        'details_cooperative' : details_cooperative,
    }
    return HttpResponse(template.render(context, request))

# Details des membres 
def details_membre(request, id):
    details_membre = Membre.objects.get(id=id)
    template = loader.get_template('details/details_membre.html')
    context = {
        'details_membre' : details_membre
    }
    return HttpResponse(template.render(context, request))

# Fonction de suppression de la cooperative
# Suppression d'un membre
def supprimer_membre(request, membre_id):
    membre = get_object_or_404(Membre, id=membre_id)
    membre.delete()
    #messages.success(request, "Membre supprimé avec succès.")
    return redirect('accounts:dashboard')  # Redirige vers le dashboard

# Suppression d'une coopérative
def supprimer_cooperative(request, cooperative_id):
    cooperative = get_object_or_404(Cooperative, id=cooperative_id)
    cooperative.delete()
    #messages.success(request, "Coopérative supprimée avec succès.")
    return redirect('accounts:dashboard')  # Redirige vers le dashboard


# Modifier les informations du membre 
def modifier_membre(request, membre_id):
    membre = get_object_or_404(Membre, id=membre_id)
    if request.method == "POST":
        form = MembreForm(request.POST, instance=membre)
        if form.is_valid():
            form.save()
            #messages.success(request, "Membre mis à jour avec succès.")
            return redirect('accounts:dashboard')
    else:
        form = MembreForm(instance=membre)

    return render(request, 'edit/modifier_membre.html', {'form': form})

# Mettre à jour les informations de la coopérative


def modifier_cooperative(request, cooperative_id):
    cooperative  = get_object_or_404(Cooperative, id=cooperative_id)
    if request.method == "POST":
        form = CooperativeForm(request.POST, instance=cooperative)
        if form.is_valid():
            form.save()
            #messages.success(request, "Coopérative mise à jour avec succès.")
            return redirect('accounts:dashboard')
    else:
        form = CooperativeForm(instance=cooperative)
    return render(request, 'edit/modifier_cooperative.html', {'form': form})



def register(request):
    if request.method == 'POST':
        form = InscriptionMembreForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('confirmation-inscription')
    else:
        form = InscriptionMembreForm()
    
    return render(request, 'Inscriptions/register.html', {'form': form})


# Fonction de confirmation d'inscription de l'utilisateur 
def confirmation_inscription(request):
    """Page de confirmation après soumission du formulaire"""
    return render(request, 'Inscriptions/confirmation_inscription.html')














