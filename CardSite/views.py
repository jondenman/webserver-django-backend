from django.shortcuts import render
from CardSite.models import Product
from CardSite.serializers import ProductSerializer
from django.http import JsonResponse

# Create your views here.
def cards(request):
    #invoke serializer
    data = Product.objects.all()
    serializer = ProductSerializer(data, many=True)
    return JsonResponse({'cards': serializer.data})

def card(request, id):
    data = Product.objects.get(pk=id)
    serializer = ProductSerializer(data)
    return JsonResponse({'card': serializer.data})