from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import viewsets, permissions, status
from rest_framework.decorators import action
from rest_framework.views import APIView
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
#Importamos nuestro modelo.
from .models import Property
#Importamos nuestro serializer 
from .serializers import PropertySerializer

#Creamos las vistas
class PropertyViewSet(viewsets.ModelViewSet):
    queryset = Property.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = PropertySerializer

    #Definimos el endpoint para listar
    @action(detail=False, methods=['get'], url_path='listing')
    def list_all_properties(self, request):
        properties = Property.objects.all()
        serializer = self.get_serializer(properties, many=True)
        return Response(serializer.data)
    
    #Definimos el endpoint para devolver una propiedad
    @action(detail=True, methods=['get'], url_path='retrieve_property')
    def retrieve_single_property(self, request, pk=None):
        property_instance = self.get_object()
        serializer = self.get_serializer(property_instance)
        return Response(serializer.data)
    
    #Definimos el endpoint para crear una propiedad
    @action(detail=False, methods=['post'], url_path='create')
    def create_property(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    

    #Definimos el endpoint para actualizar 
    @action(detail=True, methods=['put'], url_path='update')
    def update_property(self, request, pk=None):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    #Definimos el endpoint para eliminar
    @action(detail=True, methods=['delete'], url_path='delete')
    def delete_property(self, request, pk=None):
        instance = self.get_object()
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
