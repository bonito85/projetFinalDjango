from django.db import models
from django.contrib.auth.models import AbstractUser


# Créer un utilisateur pour l'authentification

class User(AbstractUser):
    