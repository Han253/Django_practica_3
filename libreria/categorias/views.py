from django.shortcuts import render

#Rest Imports
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Categoria
from .serializers import CategoriaSerializer

# Create your views here.
class CategoriaListApiView(APIView):

    def get(self,request,*args, **kwargs):
        '''
        Lista todas las categorias en base de datos
        '''
        categorias = Categoria.objects.all()
        serializer = CategoriaSerializer(categorias, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
