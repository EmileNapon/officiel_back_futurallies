# views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from .models import Enterprise, Offer, File, OfferApplication
from .serializers import EnterpriseSerializer, OfferSerializer, FileSerializer, OfferApplicationSerializer
from rest_framework.decorators import api_view
# class FileView1(APIView):
#     def post(self, request):
#         file = request.FILES.get('file')
#         if not file:
#             return Response({'error': 'No file provided'}, status=status.HTTP_400_BAD_REQUEST)

#         file_data = {
#             'title': request.data.get('title', file.name),
#             'file_type': file.content_type,
#             'file_size': file.size,
#             'file_content': file.read(),  # Read the binary content of the file
#         }

#         serializer = FileSerializer(data=file_data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser
from .models import File
from .serializers import FileSerializer

from rest_framework.parsers import MultiPartParser, FormParser
from .models import File
from .serializers import FileSerializer

class FileView(APIView):

    parser_classes = [MultiPartParser, FormParser]  # Pour gérer les fichiers

    def post(self, request, *args, **kwargs):
        file = request.FILES.get('file')
        
        if not file:
            return Response({'error': 'No file provided'}, status=status.HTTP_400_BAD_REQUEST)

        file_data = {
            'title': request.data.get('title', file.name),
            'file_type': file.content_type,
            'file_size': file.size,
            'file_content': file.read(),  # Lecture du contenu binaire
        }

        serializer = FileSerializer(data=file_data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, *args, **kwargs):
        files = File.objects.all()
        serializer = FileSerializer(files, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    

class FileView2(APIView):
    def get(self, request):
        files = File.objects.all()
        serializer = FileSerializer(files, many=True)
        return Response(serializer.data)


class FileDetailView(APIView):
    def get(self, request, pk):
        file = get_object_or_404(File, pk=pk)
        serializer = FileSerializer(file)
        return Response(serializer.data)

    def delete(self, request, pk):
        file = get_object_or_404(File, pk=pk)
        file.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



class EnterpriseView(APIView):
    def post(self, request):
        serializer = EnterpriseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        enterprises = Enterprise.objects.all()
        serializer = EnterpriseSerializer(enterprises, many=True)
        return Response(serializer.data)


class EnterpriseDetailView(APIView):
    def get(self, request, pk):
        enterprise = get_object_or_404(Enterprise, pk=pk)
        serializer = EnterpriseSerializer(enterprise)
        return Response(serializer.data)

    def put(self, request, pk):
        enterprise = get_object_or_404(Enterprise, pk=pk)
        serializer = EnterpriseSerializer(enterprise, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        enterprise = get_object_or_404(Enterprise, pk=pk)
        enterprise.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class OfferView(APIView):
    def post(self, request):
        serializer = OfferSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        offers = Offer.objects.all()
        serializer = OfferSerializer(offers, many=True)
        return Response(serializer.data)


class OfferDetailView(APIView):
    def get(self, request, pk):
        offer = get_object_or_404(Offer, pk=pk)
        serializer = OfferSerializer(offer)
        return Response(serializer.data)

    def put(self, request, pk):
        offer = get_object_or_404(Offer, pk=pk)
        serializer = OfferSerializer(offer, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        offer = get_object_or_404(Offer, pk=pk)
        offer.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

from rest_framework.response import Response
from rest_framework import status
from .models import OfferApplication

class OfferApplicationView(APIView):
    def post(self, request):
        # Récupérer les fichiers envoyés
        files = request.FILES.getlist('files')
        uploaded_files = []

        # Sauvegarde des fichiers
        for file in files:
            file_data = {
                'title': file.name,
                'file_type': file.content_type,
                'file_size': file.size,
                'file_content': file.read(),
            }
            file_serializer = FileSerializer(data=file_data)
            if file_serializer.is_valid():
                saved_file = file_serializer.save()
                uploaded_files.append(saved_file.id)
            else:
                return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        # Récupérer les données de la candidature
        offer_id = request.data.get('offerId')
        candidat_id = request.data.get('candidatId')

        # Vérifier si la combinaison offerId et candidatId existe déjà
        if OfferApplication.objects.filter(offer_id=offer_id, candidat_id=candidat_id).exists():
            return Response(
                {"non_field_errors": ["This candidate has already applied for this offer."]},
                status=status.HTTP_400_BAD_REQUEST
            )

        # Créer une nouvelle candidature
        application_data = {
            'offer_id': offer_id,
            'candidat_id': candidat_id,
            'message': request.data.get('message'),
            'submitted_documents_ids': uploaded_files,
        }

        application_serializer = OfferApplicationSerializer(data=application_data)

        if application_serializer.is_valid():
            application_serializer.save()
            return Response(application_serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(application_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


from rest_framework.generics import ListAPIView
class OfferApplicationView1(ListAPIView):
    serializer_class = OfferApplicationSerializer

    def get_queryset(self):
        offer_id = self.kwargs.get('pk')  # Utilisez `pk` comme une clé de filtre personnalisée
        return OfferApplication.objects.filter(offer_id=offer_id)

class OfferApplicationDetailView(APIView):
    def get(self, request, pk):
        application = get_object_or_404(OfferApplication, pk=pk)
        serializer = OfferApplicationSerializer(application)
        return Response(serializer.data)

    def delete(self, request, pk):
        application = get_object_or_404(OfferApplication, pk=pk)
        application.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
