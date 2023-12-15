from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import viewsets, permissions, status
#Importamos nuestro modelo.
from .models import Property
#Importamos nuestro serializer 
from .serializers import PropertySerializer

#Creamos las vistas
class PropertyViewSet(viewsets.ModelViewSet):
    queryset = Property.objects.all()
    #permission_classes = [permissions.AllowAny]
    serializer_class = PropertySerializer

    #Definimos el endpoint para listar
    def listing(self, request, *args, **kwargs):
        properties = Property.objects.all()
        serializer = self.get_serializer(properties, many=True)
        return Response(serializer.data)
    
    #Definimos el endpoint para devolver una propiedad
    def retrieving(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)
    
    #Definimos el endpoint para crear una propiedad
    def creating(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    #Definimos el endpoint para actualizar 
    def updating(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    
    #Definimos el endpoint para eliminar
    def destroying(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
