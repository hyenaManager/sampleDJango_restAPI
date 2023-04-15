from rest_framework import serializers
from .models import Book,Author

class Book_serializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ('__all__')

class Author_serializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ('__all__')