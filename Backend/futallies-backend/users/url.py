from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView
from .views import (
    CustomTokenObtainPairView, RegisterView, UserDetailView, 
    list_users, UpdateUserView, DeleteUserView
)

urlpatterns = [
    # Authentification et inscription
    path('fidalli/register/', RegisterView.as_view(), name='register'),
    path('fidalli/login/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # Gestion des utilisateurs
    path('fidalli/users/', list_users, name='list_users'),  # Liste des utilisateurs
    path('fidalli/users/me/', UserDetailView.as_view(), name='user-detail'),  # Infos utilisateur connecté
    path('fidalli/users/me/update/', UpdateUserView.as_view(), name='update-user'),  # Mise à jour de l'utilisateur connecté
    path('fidalli/users/me/delete/', DeleteUserView.as_view(), name='delete-user'),  # Suppression du compte utilisateur
]

# Ajout du support pour servir les fichiers médias en mode DEBUG
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
