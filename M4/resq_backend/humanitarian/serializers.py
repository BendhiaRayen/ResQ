from rest_framework import serializers
from .models import Volunteer,Resource,Shelter,MissingPerson
class VolunteerSerializer(serializers.ModelSerializer):
    class Meta: model=Volunteer; fields='__all__'
    def validate_skills(self,v):
        if not v.strip(): raise serializers.ValidationError('Les compétences sont obligatoires.')
        return v
class ResourceSerializer(serializers.ModelSerializer):
    class Meta: model=Resource; fields='__all__'
    def validate_quantity(self,v):
        if v<1: raise serializers.ValidationError('La quantité doit être supérieure à zéro.')
        return v
class ShelterSerializer(serializers.ModelSerializer):
    available_places=serializers.ReadOnlyField()
    class Meta: model=Shelter; fields='__all__'
    def validate(self,d):
        if d.get('occupied',0)>d.get('capacity',0): raise serializers.ValidationError('Les places occupées dépassent la capacité.')
        return d
class MissingPersonSerializer(serializers.ModelSerializer):
    class Meta: model=MissingPerson; fields='__all__'
