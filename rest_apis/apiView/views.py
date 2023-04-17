from django.shortcuts import render
from rest_framework.views import APIView  
from rest_framework.response import Response  
from rest_framework import status  
from .models import Book,Author
from .serializer import Book_serializer,Author_serializer 
from rest_framework.decorators import api_view

@api_view(['GET'])
def getData(request):
    book = Author.objects.all()
    serializer = Author_serializer(book,many=True)
    return Response(serializer.data)

@api_view(['POST'])
def createData(request):
    author = request.data
    serializer = Author_serializer(data=author)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)
    
