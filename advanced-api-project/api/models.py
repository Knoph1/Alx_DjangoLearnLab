from django.db import models

# Create your models here.
from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=255)
    publication_year = models.IntegerField()
    author = models.ForeignKey(Author, related_name='books', on_delete=models.CASCADE)

    def __str__(self):
        return self.title
"""
Author Model:
- Represents an author with a name field.

Book Model:
- Represents a book with a title, publication year, and a foreign key linking it to an author.
- One-to-Many relationship: One Author -> Many Books.
"""
