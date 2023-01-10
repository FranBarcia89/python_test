from rest_framework import viewsets
from django.shortcuts import render
from django.http import JsonResponse
from .models import Character
from .serializers import CharacterSerializer

class CharacterViewSet(viewsets.ModelViewSet):
    queryset = Character.objects.all()
    serializer_class = CharacterSerializer

def my_view(request):
    character_name = request.GET.get('name')
    characters = Character.objects.filter(name=character_name).values(name, species, status, episode)
    
    print(f"Todos los personajes: {characters}")
    
    if character_name:
        for character in characters:
            name, species, status, episode = character

        # data = [{'name': name, 'species': species, 'status': status, 'episode': episode}]
        print(data)
        data = [{'name': character.name, 'species': character.species, 'status': character.status, 'episode': character.episode}]
        
        return JsonResponse(data, safe=False, content_type='application/json')
    else:
        data = 'No variable passed as GET'
        return JsonResponse(data, safe=False, content_type='application/json')
