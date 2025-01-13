from bookshelf.models import Book

# Create a new book instance
Book = Book(title="1984", author="George Orwell", publication_year=1949)
Book.save()

# Documenting in create.md
with open("create.md", "w") as file:
    file.write("### Create Operation\n")
    file.write("Command:\n")
    file.write("book = Book(title='1984', author='George Orwell', publication_year=1949)\n")
    file.write("book.save()\n")
    file.write("Output:\n")
    file.write("Successfully created Book instance with title '1984'.\n")
