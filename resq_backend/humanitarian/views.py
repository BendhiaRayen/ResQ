from rest_framework import viewsets
from .models import Volunteer,Resource,Shelter,MissingPerson
from .serializers import VolunteerSerializer,ResourceSerializer,ShelterSerializer,MissingPersonSerializer
class VolunteerViewSet(viewsets.ModelViewSet): queryset=Volunteer.objects.all().order_by('-created_at'); serializer_class=VolunteerSerializer
class ResourceViewSet(viewsets.ModelViewSet): queryset=Resource.objects.all().order_by('-created_at'); serializer_class=ResourceSerializer
class ShelterViewSet(viewsets.ModelViewSet): queryset=Shelter.objects.all().order_by('name'); serializer_class=ShelterSerializer
class MissingPersonViewSet(viewsets.ModelViewSet): queryset=MissingPerson.objects.all().order_by('-reported_at'); serializer_class=MissingPersonSerializer
