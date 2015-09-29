from django.shortcuts import render
from billing.models import Item, Bill
from billing.serializers import BillSerializer, ItemSerializer
from rest_framework import generics
from django.http import Http404
from rest_framework.response import Response

# Create your views here.

class BillsList(generics.ListCreateAPIView):
    queryset = Bill.objects.all()
    serializer_class = BillSerializer
    
class BillDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Bill.objects.all()
    serializer_class = BillSerializer

    def get(self, request, pk, format=None):
        try:
            bill = Bill.objects.get(pk=pk)
        except Bill.DoesNotExist:
            raise Http404
        
        serializer = BillSerializer(bill)
        
        return Response(serializer.data)
    
class ItemsList(generics.ListCreateAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    
class ItemDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    
    