from django.db import models
class Volunteer(models.Model):
    name=models.CharField(max_length=120)
    email=models.EmailField(unique=True)
    skills=models.CharField(max_length=300)
    zone=models.CharField(max_length=120)
    availability=models.BooleanField(default=True)
    created_at=models.DateTimeField(auto_now_add=True)
    def __str__(self): return self.name
class Resource(models.Model):
    TYPES=[('DONATION','Don'),('VEHICLE','Véhicule'),('FOOD','Nourriture'),('WATER','Eau'),('MEDICINE','Médicaments'),('EQUIPMENT','Équipement')]
    name=models.CharField(max_length=120); type=models.CharField(max_length=20,choices=TYPES)
    quantity=models.PositiveIntegerField(); location=models.CharField(max_length=150); available=models.BooleanField(default=True)
    created_at=models.DateTimeField(auto_now_add=True)
class Shelter(models.Model):
    name=models.CharField(max_length=120); location=models.CharField(max_length=150)
    capacity=models.PositiveIntegerField(); occupied=models.PositiveIntegerField(default=0)
    contact=models.CharField(max_length=120,blank=True)
    @property
    def available_places(self): return max(0,self.capacity-self.occupied)
class MissingPerson(models.Model):
    STATUS=[('MISSING','Missing'),('POSSIBLE_MATCH','Possible Match'),('FOUND','Found'),('CLOSED','Closed')]
    full_name=models.CharField(max_length=120); age=models.PositiveIntegerField(null=True,blank=True)
    zone=models.CharField(max_length=150); description=models.TextField(); status=models.CharField(max_length=20,choices=STATUS,default='MISSING')
    reported_at=models.DateTimeField(auto_now_add=True)
