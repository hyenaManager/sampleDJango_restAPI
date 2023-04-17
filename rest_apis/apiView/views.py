from django.shortcuts import render
from rest_framework.views import APIView  
from rest_framework.response import Response  
from rest_framework import status  
from .models import Book 
from .serializer import Book_serializer  
from rest_framework.decorators import api_view

class BookView(APIView):

    def get(self,request,*args,**kwargs):
        result = Book.objects.all()
        serializer = Book_serializer(result,many=True)
        return Response({'status': 'success', "books":serializer.data}, status=200) 
    
    def post(self,request):
        serializer1 = Book_serializer(data=request.data)  
        if serializer1.is_valid():  
            serializer1.save()  
            return Response({"status": "success", "data": serializer1.data}, status=status.HTTP_200_OK)  
        else:  
            return Response({"status": "error", "data": serializer1.errors}, status=status.HTTP_400_BAD_REQUEST) 
