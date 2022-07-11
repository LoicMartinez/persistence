from rest_framework import serializers

from app.components.marque.model import Marque
from app.components.voiture.serializer import VoitureSerializer


class MarqueSerializer(serializers.ModelSerializer):
    voitures = VoitureSerializer(many=True, read_only=True)

    class Meta:
        model = Marque
        fields = ('id', 'name', 'voitures')
