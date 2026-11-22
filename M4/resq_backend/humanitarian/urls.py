from rest_framework.routers import DefaultRouter
from .views import VolunteerViewSet,ResourceViewSet,ShelterViewSet,MissingPersonViewSet
router=DefaultRouter(); router.register('volunteers',VolunteerViewSet); router.register('resources',ResourceViewSet); router.register('shelters',ShelterViewSet); router.register('missing-persons',MissingPersonViewSet)
urlpatterns=router.urls
