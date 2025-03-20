import logging
from django.conf import settings
from django.shortcuts import render

# Create your views here.
from rest_framework.viewsets import ModelViewSet
from .models import Quiz, Question, Options, Reponse
from .serializers import QuizSerializer, QuestionSerializer, OptionsSerializer, ReponseSerializer
# from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated

# --------------------
from rest_framework.views import APIView
from rest_framework.generics import get_object_or_404
from .models import Quiz
from .serializers import QuizSerializer



import google.generativeai as genai
import json


# ----------------- Quiz --------------------------
@api_view(['GET'])
@permission_classes([IsAuthenticated])  # Permet seulement aux utilisateurs authentifiés de lister les offres
def list_quiz(request):
    quiz = Quiz.objects.all()  # Récupérer toutes les offres
    serializer = QuizSerializer(quiz, many=True)  # Sérialiser les données
    return Response(serializer.data, status=status.HTTP_200_OK)
# --------------- Fin quiz ----------------------

class QuizViewSet(ModelViewSet):
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer


class QuestionViewSet(ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer


class OptionsViewSet(ModelViewSet):
    queryset = Options.objects.all()
    serializer_class = OptionsSerializer


class ReponseViewSet(ModelViewSet):
    queryset = Reponse.objects.all()
    serializer_class = ReponseSerializer

# ----------Recuperation d'un quiz avec tous les détails -------------------

class QuizDetailView(APIView):
    """
    API pour récupérer un quiz avec tous ses détails.
    Si aucun ID n'est spécifié, retourne le dernier quiz.
    """

    def get(self, request, pk=None):
        if pk:
            # Récupérer le quiz spécifique par ID
            quiz = get_object_or_404(Quiz, pk=pk)
        else:
            # Récupérer le dernier quiz créé
            quiz = Quiz.objects.latest('created_at')  # Trié par date de création
        # Sérialiser le quiz avec tous ses détails
        serializer = QuizSerializer(quiz)
        return Response(serializer.data)



@api_view(['POST'])
@permission_classes([IsAuthenticated])
def GenerateQuizQuestions(request):
    description = request.data.get("description", "")
    if not description:
        return Response({"error": "La description est obligatoire."}, status=status.HTTP_400_BAD_REQUEST)

    # Appel au modèle génératif
    genai.configure(api_key=settings.GEMINI_API_KEY)
    model = genai.GenerativeModel("gemini-1.5-flash")
    response = model.generate_content(description)
    generated_text = response.text

    # Retourner le texte brut généré
    return Response({"generated_text": generated_text}, status=status.HTTP_200_OK)



def format_quiz_to_json(text):

    questions = []
    current_question = None
    question_id = 0

    for line in text.splitlines():
        line = line.strip()

        # Détecter une question
        if line.startswith("**Question"):
            if current_question:
                questions.append(current_question)
            question_id += 1
            question_text = line.split(":**")[1].strip()
            question_type = "multiple" if "(Plusieurs réponses possibles)" in line else "single"
            current_question = {
                "id": question_id,
                "question": question_text,
                "type": question_type,
                "options": [],
                "reponses": [],
                "explication": "Pas d'explication fournie"  # Valeur par défaut si aucune explication n'est donnée
            }

        # Détecter les options
        elif line.startswith(("a)", "b)", "c)", "d)", "e)")):
            if current_question:
                option_id = line[0]  # Exemple: "a)" => "a"
                option_text = line[3:].strip()  # Exemple: "a) Texte de l'option"
                current_question["options"].append({
                    "option_id": option_id,
                    "option_text": option_text
                })

        # Détecter une réponse
        elif line.startswith("**Réponse:**"):
            if current_question:
                reponses = line.split("**Réponse:**")[1].strip().split(",")
                current_question["reponses"] = [rep.strip()[0] for rep in reponses]  # Stocke seulement les IDs (a, b, c)

        # Détecter une explication
        elif line.startswith("**Explication:**"):
            if current_question:
                explanation = line.split("**Explication:**")[1].strip()
                current_question["explication"] = explanation

    # Ajouter la dernière question
    if current_question:
        questions.append(current_question)

    return questions



@api_view(['POST'])
@permission_classes([IsAuthenticated])
def SaveQuiz(request):
    try:
        title = request.data.get("title")
        date = request.data.get("date")
        start_time = request.data.get("start_time")
        duration_minutes = request.data.get("duration_minutes")
        module_id = request.data.get("module_id")
        generated_text = request.data.get("description")


        # print('Vide', generated_text)
        formatted_data = format_quiz_to_json(generated_text)
       
        print("=== Données JSON formatées ===")
        print(json.dumps(formatted_data, indent=4, ensure_ascii=False))  # JSON lisible avec indentations
         
        # Création du quiz
        quiz = Quiz.objects.create(
            besoin=generated_text,
            title=title,
            date=date,
            start_time=start_time,
            duration_minutes=duration_minutes,
            module_id=module_id
        )
         

        # Insérer les questions, options et réponses dans la base de données
        for question_data in formatted_data:
            # Créer une question liée au quiz
            question = Question.objects.create(
                quiz=quiz,
                question=question_data["question"],
                type=question_data["type"],
                explication=question_data["explication"]
            )

            # Créer les options associées
            for option_data in question_data["options"]:
                Options.objects.create(
                    question=question,
                    option_id=option_data["option_id"],
                    option_text=option_data["option_text"]
                )

            # Créer les réponses associées
            for reponse_id in question_data["reponses"]:
                Reponse.objects.create(
                    question=question,
                    reponse=reponse_id
                )

        # Retourner l'ID du quiz créé
        return Response({"message": "Quiz enregistré avec succès", "quiz_id": quiz.id}, status=status.HTTP_201_CREATED)
    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
         
         
    #     print("=== Données JSON formatées ===")
        print(json.dumps(json.loads(formatted_data), indent=4, ensure_ascii=False))  # Format lisible



class QuizDetailSubmitView(APIView):
    def get(self, request, quiz_id):
        quiz = get_object_or_404(Quiz, pk=quiz_id)
        serializer = QuizSerializer(quiz)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, quiz_id):
        quiz = get_object_or_404(Quiz, pk=quiz_id)
        answers = request.data.get("answers", {})  # Format attendu : {question_id: [option_ids]}
        score = 0

        for question in quiz.questions.all():
            correct_answers = set(question.reponse_set.values_list('reponse', flat=True))
            user_answers = set(answers.get(str(question.id), []))
            if correct_answers == user_answers:
                score += 1

        return Response({"score": score, "total": quiz.questions.count()}, status=status.HTTP_200_OK)



 
