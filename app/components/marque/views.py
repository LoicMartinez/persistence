from rest_framework.response import Response
from rest_framework.decorators import api_view

from app.components.marque.serializer import MarqueSerializer
from app.components.marque.model import Marque


@api_view(['GET'])
def marque_view_set(request):
    api_urls = {
        'List': '/marque-list',
        'Detail view': '/marque-detail/<int:id>',
        'Create': '/marque-create/',
        'Update': '/marque-update/<int:id>',
        'Delete': '/marque-detail/<int:id>',
    }

    return Response(api_urls)


@api_view(['GET'])
def show_all(request):
    voiture = Marque.objects.all()
    serialize = MarqueSerializer(voiture, many=True)

    return Response(serialize.data)


@api_view(['GET'])
def show_detail(request, pk):
    voiture = Marque.objects.get(id=pk)
    serializer = MarqueSerializer(voiture, many=False)

    return Response(serializer.data)


@api_view(['POST'])
def create_marque(request):
    serialier = MarqueSerializer(data=request.data)

    if serialier.is_valid():
        serialier.save()

    return Response(serialier.data)


@api_view(['POST'])
def update_marque(request, pk):
    voiture = Marque.objects.get(id=pk)
    serializer = MarqueSerializer(instance=voiture, data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['GET'])
def delete_marque(request, pk):
    voiture = Marque.objects.get(id=pk)
    voiture.delete()

    return Response('Items deleted')
