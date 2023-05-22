from rest_framework import serializers
from .models import*

class VocavularySerializer(serializers.ModelSerializer):

    class Meta:
        model = VocavularyModel
        fields = ('__all__') 
  
class ColVocavularySerializer(serializers.ModelSerializer):
    vocavulary = VocavularySerializer(many=True)

    class Meta:
        model = ColVocavularyModel
        fields = ('__all__')

