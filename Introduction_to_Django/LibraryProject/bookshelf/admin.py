from django.contrib import admin

# Register your models here.
# bookshelf/admin.py
from django.contrib import admin
from .models import Book

admin.site.register(Book)

# bookshelf/admin.py
from django.contrib import admin
from .models import Book

class BookAdmin(admin.ModelAdmin):
    # Define fields to display in the list view
    list_display = ('title', 'author', 'publication_year')
    
    # Add search functionality
    search_fields = ('title', 'author__name')  # Assuming 'author' is a foreign key to an Author model
    
    # Add filters for easy categorization
    list_filter = ('publication_year', 'author')

# Register the Book model with the customized admin class
admin.site.register(Book, BookAdmin)
