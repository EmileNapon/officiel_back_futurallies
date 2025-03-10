from django.db import models

# from App_FutturAllies.Formation.models import Module
from Formation.models import Module

# Create your models here.
# class Module(models.Model):
#     name = models.CharField(max_length=255)

#     def __str__(self):
#         return self.name


class Quiz(models.Model):
    besoin = models.TextField()
    title = models.CharField(max_length=255, blank=True, null=True)
    date = models.DateField(blank=True, null=True)
    start_time = models.TimeField(blank=True, null=True)
    duration_minutes = models.PositiveIntegerField(blank=True, null=True)
    module = models.ForeignKey(Module, on_delete=models.CASCADE, related_name="quizzes")

    def __str__(self):
        return self.title or f"Quiz #{self.id}"


# class Question(models.Model):
#     question = models.TextField()
#     explanation = models.TextField(blank=True, null=True)
#     quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, related_name="questions")

#     def __str__(self):
#         return self.question


# class Options(models.Model):
#     option_text = models.TextField()
#     question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name="options")

#     def __str__(self):
#         return self.option_text


# class Reponse(models.Model):
#     reponse = models.TextField()
#     question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name="reponses")

#     def __str__(self):
#         return self.reponse
    
class Question(models.Model):
    """
    Modèle représentant une question dans un quiz.
    """
    MULTIPLE = 'multiple'
    SINGLE = 'single'
    QUESTION_TYPES = [
        (MULTIPLE, 'Multiple'),
        (SINGLE, 'Single'),
    ]
    
    type = models.CharField(max_length=10, choices=QUESTION_TYPES, default='NotPrecison', help_text="Type de question")
    question = models.TextField(help_text="Texte de la question")
    explication = models.TextField(blank=True, null=True)
    quiz = models.ForeignKey(Quiz, related_name='questions', on_delete=models.CASCADE)

    def __str__(self):
        return self.question


class Options(models.Model):
    """
    Modèle représentant une option pour une question.
    """
    option_id = models.CharField(max_length=1, null=True, help_text="Identifiant de l'option (a, b, c, ...)")
    option_text = models.TextField(help_text="Texte de l'option")
    question = models.ForeignKey(Question, related_name='options', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.option_id}: {self.option_text}"


class Reponse(models.Model):
    """
    Modèle représentant une réponse à une question.
    """
    question = models.ForeignKey(Question, related_name='reponses', on_delete=models.CASCADE)
    # reponse = models.TextField(help_text="Texte de la réponse")
    reponse = models.CharField(max_length=1, help_text="Identifiant de l'option (a, b, c, ...)")

    def __str__(self):
        return self.reponse