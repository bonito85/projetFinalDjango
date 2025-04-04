from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required 
from cooperative.models import Cooperative, Membre
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
# connexion de l'administrateur

def login_user(request): 
    if request.method == 'POST': 
        username = request.POST.get("username") 
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)
        if user and password is not None: 
            login(request, user)
            return redirect("accounts:dashboard") 
        else:
            messages.info(request, "Nom d'utilisateur ou mot de passe invalide")  # Correction ici

    form = AuthenticationForm()
    return render(request, 'connexion/login.html', {"form": form})  # Correction ici

# Fonction de deconnexion de l'administrateur
def logout_user(request): 
    logout(request) 
    messages.info(request, "Vous êtes déconnecté")  # Correction ici
    return redirect("accounts:login")

# Connexion au dashboard
@login_required
def dashboard(request):
    return render(request, 'connexion/dashboard.html')
"""
class AdminDashboardView(LoginRequiredMixin, ListView):
    model = Cooperative
    template_name = 'connexion/dashboard.html'
    context_object_name = 'cooperatives'
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cooperatives_count'] = Cooperative.objects.count()
        context['members_count'] = Membre.objects.count()  # Si vous avez ce modèle
        return context"""
def dashboard(request):
    # Récupérer toutes les coopératives
    cooperatives = Cooperative.objects.all()
    
    # Récupérer tous les membres (ou filtrer selon vos besoins)
    membres = Membre.objects.all()
    
    # Compter le nombre de coopératives et membres
    nb_cooperatives = cooperatives.count()
    nb_membres = membres.count()
    
    context = {
        'cooperatives': cooperatives,
        'membres': membres,
        'nb_cooperatives': nb_cooperatives,
        'nb_membres': nb_membres,
    }
    return render(request, 'connexion/dashboard.html', context)

# Enregistrer un membre a la cooperative

"""
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, f"Compte créé pour {user.username}!")
            return redirect("accounts:login")
    else:
        form = UserCreationForm()
    
    return render(request, 'connexion/register.html', {"form": form})
"""
#gerer membres 
def gerer_membres(request):
    """Page de gestion des membres """
    return render(request, 'gestion/gerer_membre.html')