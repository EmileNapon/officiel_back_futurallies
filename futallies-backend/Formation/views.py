
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

from Formation.models import Domaine, Module, Cours, Chapitre,Contenu, WebinarEnrollment, Section
from .serializers import ChapitreSerializer, ContenuSerializer, CoursSerializer, DomaineSerializer, ModuleSerializer, WebinarEnrollmentSerializer, SectionSerializer
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
###################################################################################################
@api_view(['POST'])
def create_domaine(request):
    if request.method == 'POST':
        serializer = DomaineSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET'])
@permission_classes([IsAuthenticated])  # Permet seulement aux utilisateurs authentifiés de lister les offres
def list_domaines(request):
    domaines = Domaine.objects.all()  # Récupérer toutes les offres
    serializer = DomaineSerializer(domaines, many=True)  # Sérialiser les données
    return Response(serializer.data, status=status.HTTP_200_OK)


###################################################################################################
@api_view(['POST'])
def create_module(request):
    if request.method == 'POST':
        serializer = ModuleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

   
@api_view(['GET'])
@permission_classes([IsAuthenticated])  # Permet seulement aux utilisateurs authentifiés de lister les offres
def list_modules(request):
    modules = Module.objects.all()  # Récupérer toutes les offres
    serializer = ModuleSerializer(modules, many=True)  # Sérialiser les données
    return Response(serializer.data, status=status.HTTP_200_OK)

###################################################################################################

@api_view(['POST'])
def create_cours(request):
    if request.method == 'POST':
        serializer = CoursSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

@api_view(['GET'])
# @permission_classes([IsAuthenticated])  # Permet seulement aux utilisateurs authentifiés de lister les offres
def list_cours(request):
    cours= Cours.objects.all()  # Récupérer toutes les offres
    serializer = CoursSerializer(cours, many=True)  # Sérialiser les données
    return Response(serializer.data, status=status.HTTP_200_OK)

###################################################################################################
@api_view(['POST'])
def create_chapitre(request):
    if request.method == 'POST':
        serializer = ChapitreSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

@api_view(['GET'])
@permission_classes([IsAuthenticated])  # Permet seulement aux utilisateurs authentifiés de lister les offres
def list_chapitres(request):
    chapitre= Chapitre.objects.all()  # Récupérer toutes les offres
    serializer = ChapitreSerializer(chapitre, many=True)  # Sérialiser les données
    print(list_chapitres)
    return Response(serializer.data, status=status.HTTP_200_OK)
    
###################################################################################################

@api_view(['POST'])
def create_section(request):
    if request.method == 'POST':
        serializer = SectionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

@api_view(['GET'])
# @permission_classes([IsAuthenticated])  # Permet seulement aux utilisateurs authentifiés de lister les offres
def list_section(request):
    section= Section.objects.all()  # Récupérer toutes les offres
    serializer = SectionSerializer(section, many=True)  # Sérialiser les données
    return Response(serializer.data, status=status.HTTP_200_OK)

###################################################################################################

@api_view(['POST'])
def create_contenu(request):
    if request.method == 'POST':
        serializer = ContenuSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    


@api_view(['GET'])
# @permission_classes([IsAuthenticated])  # Permet seulement aux utilisateurs authentifiés de lister les offres
def list_contenus(request):
    contenu= Contenu.objects.all()  # Récupérer toutes les offres
    serializer = ContenuSerializer(contenu, many=True)  # Sérialiser les données
    return Response(serializer.data, status=status.HTTP_200_OK)
###################################################################################################


#####################################################################  modification     

class ContentView(APIView):
    def get(self, request, contenu_id=None):
        contenu = get_object_or_404(Contenu, id=contenu_id)
        serializer = ContenuSerializer(contenu)
        return Response(serializer.data)


from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Contenu, Section
from .serializers import ContenuSerializer

@api_view(['PUT'])
def update_contenu(request):
    try:
        updated_contens = []
        for contenu_data in request.data:
            # Récupérer l'instance du Contenu
            contenu = Contenu.objects.get(id=contenu_data['id'])
            
            # Mettre à jour les champs
            contenu.description = contenu_data['description']
            
            # Récupérer l'instance de la Section correspondante à l'ID
            
            contenu.save()  # Sauvegarde dans la base de données
            updated_contens.append(contenu)

        # Sérialisation des objets mis à jour
        serializer = ContenuSerializer(updated_contens, many=True)
        return Response({
            'updated': serializer.data,
            'errors': []
        })
    except Exception as e:
        return Response({
            'updated': [],
            'errors': str(e)
        }, status=400)

#####################################################################  modification     

class ChapitreView(APIView):
    def get(self, request, chapitre_id):
        chapitre = get_object_or_404(Chapitre, id=chapitre_id)
        serializer = ChapitreSerializer(chapitre)
        return Response(serializer.data)





##############################################################################################
##############################################################################################
    

from .models import Webinar
from .serializers import WebinarSerializer

# Liste des webinaires (GET /fapi/webinars/)
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def list_webinars(request):
    webinars = Webinar.objects.all()
    serializer = WebinarSerializer(webinars, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

# Détails d'un webinaire (GET /fapi/webinars/<webinar_id>/)
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_webinar_detail(request, webinar_id):
    try:
        webinar = Webinar.objects.get(pk=webinar_id)
    except Webinar.DoesNotExist:
        return Response({"error": "Webinar not found"}, status=status.HTTP_404_NOT_FOUND)

    serializer = WebinarSerializer(webinar)
    return Response(serializer.data, status=status.HTTP_200_OK)



from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Webinar
from .serializers import WebinarSerializer


from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Webinar
from .serializers import WebinarSerializer

@api_view(['POST', 'PUT'])
def create_or_update_webinar(request, pk=None):
    """
    Crée un nouveau webinar (POST) ou met à jour un webinar existant (PUT).
    """
    if request.method == 'POST':
        # Création d'un nouveau webinar
        serializer = WebinarSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()  # Appelle save pour créer
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'PUT':
        # Mise à jour d'un webinar existant
        if pk is None:
            return Response({"error": "L'ID du webinar est requis pour la mise à jour."}, status=status.HTTP_400_BAD_REQUEST)
        
        try:
            webinar = Webinar.objects.get(pk=pk)
        except Webinar.DoesNotExist:
            return Response({"error": "Webinar non trouvé."}, status=status.HTTP_404_NOT_FOUND)

        serializer = WebinarSerializer(instance=webinar, data=request.data, partial=True)  # partial=True permet des mises à jour partielles
        if serializer.is_valid():
            serializer.save()  # Appelle save pour mettre à jour
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)











# Mise à jour d'un webinaire (PUT /fapi/webinars/<webinar_id>/update/)
@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def update_webinar(request, webinar_id):
    try:
        webinar = Webinar.objects.get(pk=webinar_id)
    except Webinar.DoesNotExist:
        return Response({"error": "Webinar not found"}, status=status.HTTP_404_NOT_FOUND)

    serializer = WebinarSerializer(webinar, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Suppression d'un webinaire (DELETE /fapi/webinars/<webinar_id>/delete/)
@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_webinar(request, webinar_id):
    try:
        webinar = Webinar.objects.get(pk=webinar_id)
      
    except Webinar.DoesNotExist:
        return Response({"error": "Webinar not found"}, status=status.HTTP_404_NOT_FOUND)

    webinar.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.core.mail import send_mail
from django.conf import settings
from .models import WebinarEnrollment, CustomUser
from .serializers import WebinarEnrollmentSerializer

@api_view(['POST'])
def enroll_to_webinar(request):
    # Sérialiser les données de l'inscription
    serializer = WebinarEnrollmentSerializer(data=request.data)
    
    if serializer.is_valid():
        # Récupérer le webinaire et l'ID de l'utilisateur
        webinar = serializer.validated_data['webinarId']
        user_id = request.data.get('user')  # Récupérer l'ID de l'utilisateur
        
        # Vérifier si l'utilisateur existe
        try:
            # Assurez-vous que l'utilisateur existe et récupérez-le
            user = CustomUser.objects.get(id=user_id)
        except CustomUser.DoesNotExist:
            return Response(
                {"message": "L'utilisateur spécifié n'existe pas."},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        # Vérifier si l'utilisateur est déjà inscrit à ce webinaire
        if WebinarEnrollment.objects.filter(user=user, webinarId=webinar).exists():
            return Response(
                {"message": f"L'utilisateur {user.nom} est déjà inscrit à ce webinaire."},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        # Sauvegarder l'inscription avec l'objet utilisateur
        serializer.save(user=user)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)





@api_view(['GET'])
@permission_classes([IsAuthenticated])
def list_webinars_inscrit(request):
    webinars = WebinarEnrollment.objects.all()
    serializer = WebinarEnrollmentSerializer(webinars, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)