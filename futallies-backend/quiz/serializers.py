from rest_framework import serializers
from .models import Quiz, Question, Options, Reponse



class OptionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Options
        fields = "__all__"


class ReponseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reponse
        fields = "__all__"


class QuestionSerializer(serializers.ModelSerializer):
    options = OptionsSerializer(many=True, read_only=True)
    reponses = ReponseSerializer(many=True, read_only=True)

    class Meta:
        model = Question
        fields = "__all__"


class QuizSerializer(serializers.ModelSerializer):
    questions = QuestionSerializer(many=True, read_only=True)

    class Meta:
        model = Quiz
        fields = "__all__"

# class OptionsSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Options
#         fields = "__all__"


# class ReponseSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Reponse
#         fields = "__all__"


# class QuestionSerializer(serializers.ModelSerializer):
#     options = OptionsSerializer(many=True, required=False)
#     reponses = ReponseSerializer(many=True, required=False)

#     class Meta:
#         model = Question
#         fields = "__all__"


# class QuizSerializer(serializers.ModelSerializer):
#     questions = QuestionSerializer(many=True, required=False)

#     class Meta:
#         model = Quiz
#         fields = "__all__"
#         # -----------------------------------------------------------------------
