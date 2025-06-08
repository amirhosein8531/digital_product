from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import render
from rest_framework import status, viewsets

from .models import Category,Product,File
from .serializers import CategorySerializer,ProductSerializer,FileSerializer

class Productlistview(APIView):
    def get(self,request):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

