from django.http import JsonResponse
from django.urls import path, include

def home(request):
    return JsonResponse({
        'application': 'ResQ',
        'module': 'M4 - Aide humanitaire',
        'message': 'API opérationnelle',
        'endpoints': ['/api/volunteers/', '/api/resources/', '/api/shelters/', '/api/missing-persons/']
    })

urlpatterns=[path('', home), path('api/',include('humanitarian.urls'))]
