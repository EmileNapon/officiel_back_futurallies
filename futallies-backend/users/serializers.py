from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from .models import CustomUser

# Serializer d'inscription
class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, min_length=6)
    
    class Meta:
        model = CustomUser
        fields = ['email', 'nom', 'prenom', 'phone_number', 'role', 'password', 'fonction', 'specialite', 'profile_pic']
        extra_kwargs = {
            'role': {'required': False},  # Role n'est pas obligatoire
        }

    def validate_email(self, value):
        """ Vérifier l'unicité de l'email """
        if CustomUser.objects.filter(email=value).exists():
            raise serializers.ValidationError("Cet email est déjà utilisé.")
        return value

    def create(self, validated_data):
        password = validated_data.pop('password')
        profile_pic = validated_data.pop('profile_pic', None)
        role = validated_data.get('role', 'apprenant')  # Rôle par défaut : apprenant
        email = validated_data.pop('email')

        # Vérification si un superadmin existe déjà
        if role == 'admin' and CustomUser.objects.filter(is_superuser=True).exists():
            raise serializers.ValidationError("Un administrateur existe déjà.")

        # Création de l'utilisateur avec la gestion des rôles
        if role == 'admin':
            user = CustomUser.objects.create_superuser(email=email, password=password, **validated_data)
        else:
            user = CustomUser.objects.create_user(email=email, password=password, **validated_data)

        # Ajout de l'image de profil
        if profile_pic:
            user.profile_pic = profile_pic
            user.save(update_fields=['profile_pic'])

        return user


# Serializer pour la mise à jour d'un utilisateur
class UpdateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['nom', 'prenom', 'phone_number', 'role', 'fonction', 'specialite', 'profile_pic']
        extra_kwargs = {
            'role': {'read_only': True},  # On ne permet pas de changer le rôle
        }


# Serializer pour obtenir un token avec des informations supplémentaires
class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Ajout des informations utilisateur au token
        token['id'] = user.id
        token['nom'] = user.nom
        token['prenom'] = user.prenom
        token['role'] = user.role
        token['email'] = user.email
        token['is_superuser'] = user.is_superuser
        token['fonction'] = user.fonction
        token['specialite'] = user.specialite
        if user.profile_pic:
            token['profile_pic'] = user.profile_pic.url  # Récupération de l'URL de l'image de profil

        return token

    def validate(self, attrs):
        data = super().validate(attrs)
        user = self.user  # Utilisateur authentifié par super().validate()

        # Ajout des données utilisateur à la réponse du token
        data.update({
            'id': user.id,
            'nom': user.nom,
            'prenom': user.prenom,
            'role': user.role,
            'email': user.email,
            'is_superuser': user.is_superuser,
            'fonction': user.fonction,
            'specialite': user.specialite,
            'profile_pic': user.profile_pic.url if user.profile_pic else None,
        })
        return data


# Serializer pour récupérer les informations d'un utilisateur
class UserSerializer(serializers.ModelSerializer):
    profile_pic = serializers.ImageField(use_url=True, required=False)

    class Meta:
        model = CustomUser
        fields = ['id', 'email', 'nom', 'prenom', 'phone_number', 'role', 'is_superuser', 'fonction', 'specialite', 'profile_pic']
        read_only_fields = ['id', 'is_superuser']
