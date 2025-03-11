from rest_framework import serializers
from .models import Enterprise, Offer, File, OfferApplication

class EnterpriseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Enterprise
        fields = '__all__'


class OfferSerializer(serializers.ModelSerializer):
    class Meta:
        model = Offer
        fields = '__all__'


class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = File
        fields = '__all__'


class OfferApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = OfferApplication
        fields = '__all__'
