from django.shortcuts import render
from rest_framework.views import APIView  
from rest_framework.response import Response  
from rest_framework import status  
from .models import Book 
from .serializer import Book_serializer  
from rest_framework.decorators import api_view

@api_view(['GET'])
def getData(request):
    book = Book.objects.all()
    serializer = Book_serializer(book,many=True)
    return Response(serializer.data)

@api_view(['POST'])
def createData(request):
    book = request.data
    serializer = Book_serializer(book)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)
