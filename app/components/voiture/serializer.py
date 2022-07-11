from rest_framework import serializers

from app.components.voiture.model import Voiture


class VoitureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Voiture
        fields = ('id', 'name', 'color', 'marque_id')
