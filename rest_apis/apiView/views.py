from django.shortcuts import render
from rest_framework.views import APIView  
from rest_framework.response import Response  
from rest_framework import status  
from .models import Book 
from .serializer import Book_serializer  
from rest_framework.decorators import api_view

@api_view(['GET'])
def get(request):
    book = Book.objects.all()
    serializer = Book_serializer(book,many=True)
    return Response(serializer)
