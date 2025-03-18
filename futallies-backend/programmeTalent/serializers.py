
from rest_framework import serializers

from .models import Formation,  Inscrit, ModuleFormation, Group, AffectationStage, Seance,CustomUser

class FormationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Formation
        fields =  '__all__' 

class InscritSerializer(serializers.ModelSerializer):
    class Meta:
        model = Inscrit
        fields = '__all__'  # Including all necessary fields

class ModuleFormationSerializer(serializers.ModelSerializer):
    class Meta:
        model = ModuleFormation
        fields = ['formation', 'module']
    
    def create(self, validated_data):
        return ModuleFormation.objects.create(**validated_data)

class SeanceSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset=CustomUser.objects.all(), many=True)
    class Meta:
        model = Seance
        fields =  '__all__'   # Including all necessary fields



class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields =  '__all__'  # Including all necessary fields

class AffectationStageSerializer(serializers.ModelSerializer):
    class Meta:
        model = AffectationStage
        fields =  '__all__'   # Including all necessary fields



##############################################
        
# serializers.py

from rest_framework import serializers
from .models import Annonce

class AnnonceSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username', read_only=True)

    class Meta:
        model = Annonce
        fields = '__all__'
# class EncadrantSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Encadrant
#         fields =  '__all__'
    