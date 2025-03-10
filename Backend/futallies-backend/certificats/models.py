from django.db import models
from users.models import CustomUser
from Formation.models import Cours, Chapitre

class Institution(models.Model):
    name =models.CharField(max_length=100)
    localisation=models.CharField(max_length=30)

class Certification(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE,)
    # institution=models.ForeignKey(Institution, on_delete=models.CASCADE)
    # Titre de la certification, maximum 200 caractères
    title = models.CharField(max_length=200)
    # Description détaillée de la certification
    description = models.TextField() 
    criteres=models.TextField( default='') 
    # prerequisites = models.TextField()

    # Niveau de la certification, utilisant des choix prédéfinis
    # Utilisation de TextChoices pour définir des niveaux (ex: Débutant, Intermédiaire, Avancé)
    level = models.CharField(
        max_length=20,
        choices=[('Beginner', 'Débutant'),('Intermediate', 'Intermédiaire'),('Advanced', 'Avancé')], 
        default='Débutant'
    )
    # Coût de la certification (type float)
    cost = models.FloatField() 
    # Date de début de validité de la certification
    dateDebutValidite = models.DateField()
    # Date de fin de validité de la certification
    dateFinValidite = models.DateField()
    # La période de validité est calculée à partir des dates de début et de fin
    # Utilisation d'un IntegerField ou d'un autre type de champ en fonction de la logique
    validityPeriod = models.IntegerField()  # Si c'est une période en années, par exemple
    # Prérequis nécessaires avant de passer la certification (ex: certifications antérieures)
    # Format de l'examen, utilisant des choix prédéfinis (ex: en ligne, en présentiel)
    examFormat = models.CharField(max_length=100, choices=[('Online', 'En ligne'),('In-person', 'En présentiel')],default='En ligne')
    # Nombre de questions dans l'examen
    # Score nécessaire pour réussir l'examen, en pourcentage (float)
    # passingScore = models.FloatField()  # Corrected to FloatField

class prerequisites(models.Model):
    certification=models.ForeignKey(Certification, on_delete=models.CASCADE)
    chapitre=models.ForeignKey(Chapitre, on_delete=models.CASCADE)

class Question(models.Model):
    texte = models.TextField()
    chapitre = models.ForeignKey(Chapitre,related_name='questions',on_delete=models.CASCADE)

    def __str__(self):
        return self.texte


class Option(models.Model):
    texte = models.TextField()
    correct = models.BooleanField()
    question = models.ForeignKey(Question,related_name='options',on_delete=models.CASCADE)

    def __str__(self):
        return self.texte

class Exam(models.Model):
    # certification = models.ForeignKey(Certification, on_delete=models.CASCADE, related_name='candidates')
    date =models.DateField()
    score =models.FloatField()
    status= models.CharField(max_length=20,choices=[('passed', 'Passed'),('failed', 'Failed')],default='Passed') 
    numberOfQuestions = models.IntegerField(default=30)  # Corrected to IntegerField



class CoursUseCertification(models.Model):
    # Foreign key to Certification (one Certification can be linked to many Courses)
    certification = models.ForeignKey(Certification, on_delete=models.CASCADE, related_name='cours_certifications')
    # Foreign key to Cours (one Cours can be linked to many Certifications)
    cours = models.ForeignKey(Cours, on_delete=models.CASCADE, related_name='certifications_courses')
    # Date when this certification-course relationship was created
    createDate = models.DateField(auto_now_add=True)  # Automatically sets the date when the record is created
    # Optional: If you want to track additional attributes, such as the status of the relationship
    # Example: If the course is mandatory or optional for the certification
    is_mandatory = models.BooleanField(default=True)  # Indicates whether the course is mandatory for the certification
    # Optional: If you want to track the duration of the course related to the certification
    course_duration = models.IntegerField(null=True, blank=True)  # Duration of the course in hours or days (optional)
    # Optional: Status to track whether the certification-course relationship is active or expired
    status = models.CharField(max_length=20, choices=[('Active', 'Active'), ('Expired', 'Expired')], default='Active')


class Candidate(models.Model):
    # Lien avec l'utilisateur
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    # Lien avec une certification
    certification = models.ForeignKey(Certification, on_delete=models.CASCADE)
    # Date de souscription
    subscription_date = models.DateField(auto_now_add=True)
    # Statut du candidat par rapport à la certification
    status = models.CharField(max_length=20,choices=[('Subscribed', 'Subscribed'),('Completed', 'Completed'),('Pending', 'Pending'),],default='Subscribed')
    # Score global pour la certification
    score = models.FloatField(null=True, blank=True)
   
    def __str__(self):
        return f"{self.Candidate.user} - {self.Candidate.certification}"



class ReponseUtilisateur(models.Model):
    # Lien avec l'utilisateur
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    chapitre = models.ForeignKey(Chapitre,related_name='reponseUtilisateur',on_delete=models.CASCADE)

    # Lien avec la question
    question = models.ForeignKey(Question,related_name='reponses',on_delete=models.CASCADE)
    # Option choisie par l'utilisateur
    choix = models.ForeignKey(Option, on_delete=models.CASCADE)
    # Date de la réponse
    #date_reponse = models.DateTimeField(auto_now=True)

    class Meta:
        # Contrainte pour éviter les doublons par utilisateur et question
        unique_together = ('user', 'question')

    # def __str__(self):
    #     return f"User {self.user.username} - Question {self.question.id} - Choix {self.choix.id}"
    

class Progression(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    chapitre = models.ForeignKey(Chapitre, on_delete=models.CASCADE)
    score = models.FloatField(default=0.0)
    valide = models.BooleanField(default=False)
    tentative = models.PositiveIntegerField(default=0)





