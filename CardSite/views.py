from django.shortcuts import render
from CardSite.models import Product
from CardSite.serializers import ProductSerializer
from django.http import JsonResponse, Http404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

# Create your views here.
@api_view(['GET', 'POST'])
def cards(request):
    #invoke serializer
    data = Product.objects.all()
    serializer = ProductSerializer(data, many=True)
    if request.method == 'GET':
        return Response({'cards': serializer.data})
    elif request.method == 'POST':
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'card': serializer.data}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST', 'DELETE'])
def card(request, id):
    try:
        data = Product.objects.get(pk=id)
    except Product.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = ProductSerializer(data)
        return Response({'card': serializer.data})
    elif request.method == 'DELETE':
        data.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    elif request.method == 'POST':
        serializer = ProductSerializer(data, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'card': serializer.data})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)