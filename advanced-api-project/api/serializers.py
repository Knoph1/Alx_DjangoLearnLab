from rest_framework import serializers
from .models import Author, Book
from datetime import datetime

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'

    def validate_publication_year(self, value):
        if value > datetime.now().year:
            raise serializers.ValidationError("Publication year cannot be in the future.")
        return value

class AuthorSerializer(serializers.ModelSerializer):
    books = BookSerializer(many=True, read_only=True)

    class Meta:
        model = Author
        fields = ['name', 'books']

"""
BookSerializer:
- Serializes all fields of the Book model.
- Includes custom validation for publication_year to ensure it is not in the future.

AuthorSerializer:
- Serializes the name of the author.
- Dynamically includes a nested BookSerializer to serialize related books.
"""
