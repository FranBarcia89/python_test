from django.shortcuts import render
from rest_framework import viewsets
from .models import Character
from .serializers import CharacterSerializer
from django.http import HttpResponse

class CharacterViewSet(viewsets.ModelViewSet):
    queryset = Character.objects.all()
    serializer_class = CharacterSerializer

def my_view(request):
    name = request.GET.get('name')
    
    if name:
        return HttpResponse(f'Hello, {name}!')
    else:
        return HttpResponse('Hello, anonymous!')
