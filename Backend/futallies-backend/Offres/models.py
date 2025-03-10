from django.db import models
from datetime import date

from users.models import CustomUser

########################################################################################

class Enterprise(models.Model):
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    recruitment_email = models.EmailField()
    SIZE_CHOICES = [
        ('Small', 'Small'),
        ('Medium', 'Medium'),
        ('Large', 'Large'),
    ]
    size = models.CharField(max_length=10, choices=SIZE_CHOICES)
    website = models.URLField()
    description = models.TextField(blank=True, null=True)
    industry = models.CharField(max_length=255, blank=True, null=True)
    founded_year = models.PositiveIntegerField(blank=True, null=True)
    headquarters_location = models.CharField(max_length=255, blank=True, null=True)
    number_of_employees = models.PositiveIntegerField(blank=True, null=True)
    company_culture = models.TextField(blank=True, null=True)
    social_media_links = models.JSONField(blank=True, null=True)  # Use JSONField for a flexible mapping
    rating = models.DecimalField(max_digits=2, decimal_places=1, blank=True, null=True)
    awards_and_recognition = models.JSONField(blank=True, null=True)
    benefits_overview = models.TextField(blank=True, null=True)
    logo_url = models.URLField(blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


from django.db import models
from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Offer(models.Model):
    TYPE_CHOICES = [
        ('Job', 'Job'),
        ('Internship', 'Internship'),
        ('Other', 'Other'),
    ]

    CONTRACT_TYPE_CHOICES = [
        ('CDI', 'CDI'),
        ('CDD', 'CDD'),
    ]

    STATUS_CHOICES = [
        ('Open', 'Open'),
        ('Closed', 'Closed'),
        ('Pending', 'Pending'),
    ]

    APPLICATION_MODE_CHOICES = [
        ('Online', 'Online'),
        ('Physical', 'Physical'),
        ('Both', 'Both'),
    ]

    title = models.CharField(max_length=255, verbose_name="Titre de l'offre", null=True)
    enterprise = models.CharField(max_length=255, verbose_name="Entreprise")
    enterpriseLocation = models.CharField(max_length=255, verbose_name="Localisation de l'entreprise", null=True)
    enterWebsite = models.URLField(blank=True, null=True, verbose_name="Site web de l'entreprise")
    description = models.TextField(verbose_name="Description de l'offre", null=True)
    domain = models.CharField(max_length=255, verbose_name="Domaine de l'offre", null=True)
    location = models.CharField(max_length=255, verbose_name="Localisation de l'offre", null=True)
    salary = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True, verbose_name="Salaire")
    duration = models.IntegerField(blank=True, null=True, verbose_name="Durée (en mois)")
    type = models.CharField(max_length=20, choices=TYPE_CHOICES, verbose_name="Type d'offre")
    requirements = models.TextField(blank=True, null=True, verbose_name="Exigences")
    responsibilities = models.TextField(blank=True, null=True, verbose_name="Responsabilités")
    educationLevel = models.CharField(max_length=255, blank=True, null=True, verbose_name="Niveau d'éducation requis")
    experienceLevel = models.CharField(max_length=255, blank=True, null=True, verbose_name="Niveau d'expérience requis")
    contractType = models.CharField(max_length=3, choices=CONTRACT_TYPE_CHOICES, default='CDD', verbose_name="Type de contrat")
    benefits = models.TextField(blank=True, null=True, verbose_name="Avantages")
    contactEmail = models.EmailField(verbose_name="Email de contact", null=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='Open', verbose_name="Statut de l'offre")
    isRemote = models.BooleanField(default=False, verbose_name="Télétravail")
    applicationMode = models.CharField(max_length=10, choices=APPLICATION_MODE_CHOICES, default='Online', verbose_name="Mode de candidature")
    onlineSubmission = models.BooleanField(default=True, verbose_name="Soumission en ligne")
    isRequiredCvDoc = models.BooleanField(default=True, verbose_name="CV requis")
    isRequiredMlDoc = models.BooleanField(default=False, verbose_name="Lettre de motivation requise")
    canAddOthersDoc = models.BooleanField(default=False, verbose_name="Autres documents autorisés")
    applicationLink = models.URLField(blank=True, null=True, verbose_name="Lien de candidature")
    additionalInfo = models.TextField(blank=True, null=True, verbose_name="Informations supplémentaires")
    createdBy = models.ForeignKey(User, on_delete=models.CASCADE, related_name='offers', verbose_name="Créé par", default='16')
    postedDate = models.DateTimeField(auto_now_add=True, verbose_name="Date de publication", null=True)
    updatedAt = models.DateTimeField(auto_now=True, verbose_name="Dernière mise à jour", null=True)
    expirationDate = models.DateTimeField(blank=True, null=True, verbose_name="Date d'expiration")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Offre"
        verbose_name_plural = "Offres"


class OfferApplication(models.Model):
    offer = models.ForeignKey(Offer, on_delete=models.CASCADE, default=2)
    candidat = models.ForeignKey(CustomUser, on_delete=models.CASCADE, default=16)
    application_date = models.DateTimeField(auto_now_add=True)
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Accepted', 'Accepted'),
        ('Rejected', 'Rejected'),
        ('Review', 'Review'),
    ]
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Accepted')
    message = models.TextField(default=(
        "Je suis très intéressé(e) par cette offre et je suis convaincu(e) que mes compétences "
        "et mon expérience correspondent aux attentes de votre entreprise. J'aimerais avoir "
        "l'opportunité de discuter de cette offre plus en détail et de contribuer au succès de votre équipe."
    ))
    last_updated = models.DateTimeField(auto_now=True)
    submitted_documents_ids = models.JSONField(null=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Application by {self.candidat} for {self.offer}"
    class Meta:
        unique_together = ('offer', 'candidat')  # Assure qu'un utilisateur ne peut s'inscrire qu'une seule fois à une formation
    def __str__(self):
        return f"{self.candidat} inscrit à {self.offer}"


class File(models.Model):
    title = models.CharField(max_length=255)
    file_type = models.CharField(max_length=50, default='application/pdf' )
    file_content = models.BinaryField()  # Contient le contenu binaire du fichier
    file_size = models.PositiveBigIntegerField()
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
