from bookshelf.models import Book


# Creating a new Book instance using Book.objects.create
book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)


# Documenting in create.md

with open("create.md", "w") as file:
    file.write("### Create Operation\n")
    file.write("Command:\n")
    file.write("book = Book(title='1984', author='George Orwell', publication_year=1949)\n")
    file.write("book.save()\n")
    file.write("Output:\n")
    file.write("Successfully created Book instance with title '1984'.\n")
