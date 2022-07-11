from django.contrib.auth.models import User, Group
from rest_framework import viewsets, permissions
from rest_framework.response import Response
from app.serializers import UserSerializer, GroupSerializer
from rest_framework.decorators import api_view

from app.components.voiture.serializer import VoitureSerializer
from app.components.voiture.model import Voiture


@api_view(['GET'])
def voiture_view_set(request):
    api_urls = {
        'List': '/voiture-list',
        'Detail view': '/voiture-detail/<int:id>',
        'Create': '/voiture-create/',
        'Update': '/voiture-update/<int:id>',
        'Delete': '/voiture-detail/<int:id>',
    }

    return Response(api_urls)


@api_view(['GET'])
def show_all(request):
    voiture = Voiture.objects.all()
    serialize = VoitureSerializer(voiture, many=True)

    return Response(serialize.data)

@api_view(['GET'])
def show_detail(request, pk):
    voiture = Voiture.objects.get(id=pk)
    serializer = VoitureSerializer(voiture, many=False)

    return Response(serializer.data)


@api_view(['POST'])
def create_voiture(request):
    import logging
    serialier = VoitureSerializer(data=request.data)
    Voiture.objects.create()

    if serialier.is_valid():
        serialier.save()

    logging.error(serialier.data)

    return Response(serialier.data)


@api_view(['POST'])
def update_voiture(request, pk):
    voiture = Voiture.objects.get(id=pk)
    import logging
    logging.error(request.data)
    serializer = VoitureSerializer(instance=voiture, data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['GET'])
def delete_voiture(request, pk):
    voiture = Voiture.objects.get(id=pk)
    voiture.delete()

    return Response('Items deleted')
