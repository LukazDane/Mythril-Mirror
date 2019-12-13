from rest_framework.serializers import ModelSerializer
from sheets.models import Character


class CharacterSerializer(ModelSerializer):
    class Meta:
        model = Character
        fields = '__all__'
