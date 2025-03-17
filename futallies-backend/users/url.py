from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView
from .views import (
    CustomTokenObtainPairView, RegisterView, UserDetailView, 
    list_users, UpdateUserView, DeleteUserView, ApprenantListView, ApprenantDetailView, EncadrantListView, EncadrantDetailView,

    EntreprisesListView, EntrepriseDetailView
)

urlpatterns = [
    # Authentification et inscription
    path('fidalli/register/', RegisterView.as_view(), name='register'),
    path('fidalli/login/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # Gestion des utilisateurs
    path('fidalli/users/', list_users, name='list_users'),  # Liste des utilisateurs
    path('fidalli/users/me/', UserDetailView.as_view(), name='user-detail'),  # Infos utilisateur connecté
    path('fidalli/users/<int:pk>/', UpdateUserView.as_view(), name='update-user'),  # Mise à jour de l'utilisateur connecté
    path('fidalli/users/delete/<int:pk>/', DeleteUserView.as_view(), name='delete-user'),  # Suppression du compte utilisateur


    #filtre

     path('fidalli/apprenants/', ApprenantListView.as_view(), name='etudiant-list'),
     path('fidalli/apprenants/<int:id>/', ApprenantDetailView.as_view(), name='apprenant-detail'),

     path('fidalli/encadrants/', EncadrantListView.as_view(), name='encadrants-list'),
     path('fidalli/encadrants/<int:id>/', EncadrantDetailView.as_view(), name='encadrants-detail'),

      path('fidalli/entreprises/', EntreprisesListView.as_view(), name='employeurs-list'),
     path('fidalli/entreprises/<int:id>/', EntrepriseDetailView.as_view(), name='employeurs-detail'),
]

# Ajout du support pour servir les fichiers médias en mode DEBUG
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
