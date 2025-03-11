from rest_framework import serializers
from .models import Institution,Certification, Candidate, Exam, CoursUseCertification, Question, Option, ReponseUtilisateur, Candidate, Question, Option, ReponseUtilisateur, Progression

class InstitutionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Institution
        fields =  '__all__' 

class CertificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Certification
        fields =  '__all__' 


# Serializer pour le modèle Question
class QuestionSerializer(serializers.ModelSerializer):
    options = serializers.StringRelatedField(many=True)

    class Meta:
        model = Question
        fields = '__all__'


# Serializer pour le modèle Option
class OptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Option
        fields = '__all__'



class ExamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exam
        fields =  '__all__' 




class CoursUseCertificationSerializer(serializers.ModelSerializer):
    class Meta:
        model=CoursUseCertification
        fields='__all__'


class CandidateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Candidate
        fields =  '__all__' 



# Serializer pour le modèle ReponseUtilisateur
class ReponseUtilisateurSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReponseUtilisateur
        fields = '__all__'


class ProgressionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Progression
        fields =  '__all__' 