from django.urls import path
from . import views
#from .views import AdminDashboardView

app_name = 'accounts'

urlpatterns = [
    path('connexion/login', views.login_user, name='login'),
    path('connexion/dashboard', views.dashboard, name='dashboard'),
    path('connexion/logout', views.logout_user, name='logout'),
    #path('admin/dashboard/', AdminDashboardView.as_view(), name='admin_dashboard'),
    #path d'enregistrement
    #path('connexion/register', views.register, name='register'),
    # gerer membre 
    path('gerer-membres/', views.gerer_membres, name='gerer_membres'),
]