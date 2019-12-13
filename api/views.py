from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from sheets.models import Character
from api.serializers import CharacterSerializer
# Create your views here.


class CharacterList(APIView):
    def get(self, request):
        characters = Character.objects.all()[:20]
        data = CharacterSerializer(characters, many=True).data
        return Response(data)


class CharacterDetail(APIView):
    def get(self, request, pk):
        character = get_object_or_404(Character, pk=pk)
        data = CharacterSerializer(character).data
        return Response(data)
