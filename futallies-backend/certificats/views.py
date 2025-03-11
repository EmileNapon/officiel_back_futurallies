from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Institution, Certification, Candidate, Exam, CoursUseCertification,Chapitre
from .serializers import InstitutionSerializer, CertificationSerializer, CandidateSerializer, ExamSerializer, CoursUseCertificationSerializer
from rest_framework.viewsets import ModelViewSet
from .models import  Question, Option, ReponseUtilisateur
from .serializers import (
    QuestionSerializer,
    OptionSerializer,
    ReponseUtilisateurSerializer
)
from rest_framework.decorators import api_view
from users.models import CustomUser


# Institution View (GET and POST)
class InstitutionView(APIView):
    def get(self, request, format=None):
        institutions = Institution.objects.all()
        serializer = InstitutionSerializer(institutions, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = InstitutionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Certification View (GET and POST)
class CertificationView(APIView):
    def get(self, request, format=None):
        certifications = Certification.objects.all()
        serializer = CertificationSerializer(certifications, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = CertificationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    


class QuestionView(APIView):
    def get(self, request):
        questions = Question.objects.all()
        serializer = QuestionSerializer(questions, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = QuestionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Vue pour les options
class OptionView(APIView):
    def get(self, request):
        options = Option.objects.all()
        serializer = OptionSerializer(options, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = OptionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




# Exam View (GET and POST)
class ExamView(APIView):
    def get(self, request, format=None):
        exams = Exam.objects.all()
        serializer = ExamSerializer(exams, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ExamSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    


# Candidate View (GET and POST)
class CandidateView(APIView):
    def get(self, request, format=None):
        candidates = Candidate.objects.all()
        serializer = CandidateSerializer(candidates, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = CandidateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CoursUseCertificationView(APIView):
    def get(self, request, format=None):
        coursUseCertification = CoursUseCertification.objects.all()
        serializer = CoursUseCertificationSerializer(coursUseCertification, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = CoursUseCertificationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)







from django.utils import timezone
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import (
    CustomUser,
    Chapitre,
    Question,
    Option,
    ReponseUtilisateur
)


from django.shortcuts import get_object_or_404

class ReponseUtilisateurView(APIView):
    def get(self, request):
        reponses = ReponseUtilisateur.objects.all()
        serializer = ReponseUtilisateurSerializer(reponses, many=True)
        return Response(serializer.data)

    def post(self, request):
        try:
            data = request.data
            utilisateur_id = data.get("user")
            chapitre_id = data.get("chapitre")
            reponses = data.get("reponses")

            if not utilisateur_id or not chapitre_id or not isinstance(reponses, list):
                return Response(
                    {"error": "Données invalides. utilisateur_id, chapitre_id et une liste de réponses sont requis."},
                    status=status.HTTP_400_BAD_REQUEST
                )

            # Récupération des instances utilisateur et chapitre
            utilisateur = get_object_or_404(CustomUser, id=utilisateur_id)
            chapitre = get_object_or_404(Chapitre, id=chapitre_id)

            resultat = []

            for item in reponses:
                question_id = item.get("question")
                choix_id = item.get("choix")

                if not question_id or not choix_id:
                    return Response(
                        {"error": "Chaque réponse doit contenir une question et un choix."},
                        status=status.HTTP_400_BAD_REQUEST
                    )

                question = get_object_or_404(Question, id=question_id)
                choix = get_object_or_404(Option, id=choix_id)

                # Création ou mise à jour de la réponse utilisateur
                reponse_utilisateur, created = ReponseUtilisateur.objects.update_or_create(
                    user=utilisateur,
                    chapitre=chapitre,
                    question=question,
                    defaults={"choix": choix}
                )

                resultat.append({
                    "id": reponse_utilisateur.id,
                    "user": utilisateur.id,
                    "chapitre": chapitre.id,
                    "question": question.id,
                    "choix": choix.id
                })

            
            # Calcul du score (reste inchangé)
            questions = Question.objects.filter(chapitre_id=chapitre_id)
            total_questions = questions.count()

            if total_questions == 0:
                return Response(
                    {"error": "Aucune question disponible pour ce chapitre."},
                    status=status.HTTP_404_NOT_FOUND
                )

            reponses_utilisateur = ReponseUtilisateur.objects.filter(
                user=utilisateur, chapitre_id=chapitre_id
            )

            bonnes_reponses = sum(
                1 for reponse in reponses_utilisateur if reponse.choix.correct
            )

            score = (bonnes_reponses / total_questions) * 100 if total_questions > 0 else 0

            # Retour des réponses enregistrées et du score
            return Response(
                {
                    "reponses": resultat,
                    "score": {
                        "chapitre": chapitre_id,
                        "user": utilisateur_id,
                        "total_questions": total_questions,
                        "bonnes_reponses": bonnes_reponses,
                        "score": round(score, 2),
                    },
                },
                status=status.HTTP_200_OK,
            )


        except Exception as e:
            return Response(
                {"error": f"Une erreur est survenue : {str(e)}"},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )