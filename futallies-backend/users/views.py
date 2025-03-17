from django.shortcuts import get_object_or_404
from rest_framework import generics, status
from rest_framework.parsers import JSONParser, MultiPartParser, FormParser
from .models import CustomUser
from .serializers import (
    CustomTokenObtainPairSerializer, 
    RegisterSerializer, 
    UserSerializer, 
    UpdateUserSerializer
)
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser

# Vue pour l'inscription
class RegisterView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    permission_classes = [AllowAny]
    serializer_class = RegisterSerializer
    parser_classes = (MultiPartParser, FormParser)  # Accepte l'upload de fichiers (ex: profile_pic)

# Vue pour récupérer les informations de l'utilisateur authentifié
class UserDetailView(generics.RetrieveAPIView):
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user  # Récupère l'utilisateur connecté au lieu d'un autre utilisateur

# Vue pour la mise à jour d'un utilisateurfrom rest_framework.parsers import JSONParser, MultiPartParser, FormParser

class UpdateUserView(generics.UpdateAPIView):
    serializer_class = UpdateUserSerializer
    permission_classes = [IsAuthenticated]
    parser_classes = [JSONParser, MultiPartParser, FormParser]  # ✅ Ajout de JSONParser
    def get_object(self):
        user_id = self.kwargs.get("pk")
        return get_object_or_404(CustomUser, pk=user_id)



# Vue pour la suppression d'un utilisateur
class DeleteUserView(generics.DestroyAPIView):
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user  # Un utilisateur peut supprimer son propre compte

# Vue pour obtenir un token JWT avec des informations supplémentaires
class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer

# Vue pour lister tous les utilisateurs (nécessite une authentification)
@api_view(['GET'])
@permission_classes([IsAuthenticated])  # Seulement les utilisateurs authentifiés peuvent voir cette liste
def list_users(request):
    users = CustomUser.objects.all().order_by('-id')  # Trie les utilisateurs par ID décroissant
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


class ApprenantListView(generics.ListAPIView):
    queryset = CustomUser.objects.filter(role='apprenant')  
    serializer_class = UserSerializer


class ApprenantDetailView(generics.RetrieveAPIView):
    queryset = CustomUser.objects.filter(role='apprenant')
    serializer_class = UserSerializer
    lookup_field = 'id'  


class DeleteUserView(generics.DestroyAPIView):
    queryset = CustomUser.objects.all()
    permission_classes = [IsAuthenticated]  
    def get_object(self):
        user_id = self.kwargs.get("pk")
        return get_object_or_404(CustomUser, pk=user_id)
    



class EncadrantListView(generics.ListAPIView):
    queryset = CustomUser.objects.filter(role='formateur')  
    serializer_class = UserSerializer


class EncadrantDetailView(generics.RetrieveAPIView):
    queryset = CustomUser.objects.filter(role='formateur')
    serializer_class = UserSerializer
    lookup_field = 'id'  



class EntreprisesListView(generics.ListAPIView):
    queryset = CustomUser.objects.filter(role='employeur')  
    serializer_class = UserSerializer


class EntrepriseDetailView(generics.RetrieveAPIView):
    queryset = CustomUser.objects.filter(role='employeur')
    serializer_class = UserSerializer
    lookup_field = 'id'  