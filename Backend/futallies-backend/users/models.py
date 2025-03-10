from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models
from django.core.exceptions import ValidationError

# Custom user manager
class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('role', 'admin')

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(email, password, **extra_fields)


# Custom user model
class CustomUser(AbstractBaseUser, PermissionsMixin):
    ROLE_CHOICES = [
        ('admin', 'Admin'),
        ('apprenant', 'Apprenant'),
        ('employeur', 'Employeur'),
        ('formateur', 'Formateur'),
    ]

    nom = models.CharField(max_length=30, blank=True)
    prenom = models.CharField(max_length=30, blank=True)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=30, blank=True)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='apprenant')
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    fonction = models.TextField(max_length=200, blank=True, null=True)
    specialite = models.CharField(max_length=200, blank=True, null=True)
    profile_pic = models.ImageField(upload_to='profiles/', blank=True, null=True)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def clean(self):
        """Validation supplémentaire pour s'assurer qu'il n'y a qu'un seul superutilisateur."""
        if self.is_superuser and CustomUser.objects.filter(is_superuser=True).exclude(pk=self.pk).exists():
            raise ValidationError("Un administrateur existe déjà.")

    def save(self, *args, **kwargs):
        self.full_clean()  # Assure que clean() est appelé avant la sauvegarde
        super().save(*args, **kwargs)

    def __str__(self):
        return self.email
