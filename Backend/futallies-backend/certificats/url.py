from django.urls import path
from .views import InstitutionView, CertificationView, CandidateView, ExamView, CoursUseCertificationView, QuestionView, OptionView, ReponseUtilisateurView


urlpatterns = [
    path('institutions/', InstitutionView.as_view(), name='institution-list'),  # List and create institutions
    path('certifications/', CertificationView.as_view(), name='certification-list'),  # List and create certifications
    path('candidates/', CandidateView.as_view(), name='candidate-list'),  # List and create candidates
    path('exams/', ExamView.as_view(), name='exam-list'),  # List and create exams
    path('CoursUseCertification/', CoursUseCertificationView.as_view(), name='CoursUseCertification'),  # List and create exams

    path('questions/', QuestionView.as_view(), name='question-list'),
    path('options/', OptionView.as_view(), name='option-list'),
    path('reponses/', ReponseUtilisateurView.as_view(), name='reponse-utilisateur-list'),

]
