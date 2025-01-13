# relationship_app/query_samples.py

from .models import Author, Book, Library, Librarian

def query_books_by_author(author_name):
    try:
        author = Author.objects.get(name=author_name)
        books = Book.objects.filter(author=author)
        return books
    except Author.DoesNotExist:
        return None

def list_books_in_library(library_name):
    try:
        library = Library.objects.get(name=library_name)
        books = library.books.all()
        return books
    except Library.DoesNotExist:
        return None

def get_librarian_for_library(library_name):
    try:
        library = Library.objects.get(name=library_name)
        librarian = Librarian.objects.get(library=library)
        return librarian
    except (Library.DoesNotExist, Librarian.DoesNotExist):
        return None

# Example usage:
if __name__ == "__main__":
    # Query all books by a specific author
    author_books = query_books_by_author("Author Name")
    if author_books:
        for book in author_books:
            print(book.title)
    else:
        print("Author not found or no books available.")

    # List all books in a library
    library_books = list_books_in_library("Library Name")
    if library_books:
        for book in library_books:
            print(book.title)
    else:
        print("Library not found or no books available.")

    # Retrieve the librarian for a library
    librarian = get_librarian_for_library("Library Name")
    if librarian:
        print(f"Librarian: {librarian.name}")
    else:
        print("Library or librarian not found.")
