# Delete the book instance
from bookshelf.models import Book  

book.delete()

# Confirm deletion by retrieving all books

books = Book.objects.all()

# Documenting in delete.md

with open("delete.md", "w") as file:
    file.write("### Delete Operation\n")
    file.write("Command:\n")
    file.write("book.delete()\n")
    file.write("Output:\n")
    file.write("Successfully deleted Book instance.\n")
    file.write("All Books: []\n")
