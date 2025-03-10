from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter
from .views import GenerateQuizQuestions, QuizDetailSubmitView, QuizViewSet, QuestionViewSet, OptionsViewSet, ReponseViewSet, SaveQuiz
from .views import QuizDetailView

router = DefaultRouter()
router.register(r'quizzes', QuizViewSet)
router.register(r'questions', QuestionViewSet)
router.register(r'options', OptionsViewSet)
router.register(r'reponses', ReponseViewSet)

urlpatterns = [
    
    path('quiz/', include(router.urls)),
    path('quiz/list-quiz/', views.list_quiz, name='liste_quiz'),
    
    path('quiz/<int:pk>/', QuizDetailView.as_view(), name='quiz-detail'),
    # path('quiz/', QuizDetailView.as_view(), name='quiz-latest'),
    # path('quiz/create', QuizCreateAPIView.as_view(), name='create-quiz'),
    
    path('quiz/generate-quiz', GenerateQuizQuestions, name='genere-quiz'),
    path('quiz/save-quiz', SaveQuiz, name='save-quiz'),
    path('quiz/<quiz_id>/submit', QuizDetailSubmitView.as_view(), name='submit-response'),
]
