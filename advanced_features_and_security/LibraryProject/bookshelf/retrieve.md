# Retrieve the book instance

book = Book.objects.get(title="1984")

# Documenting in retrieve.md

with open("retrieve.md", "w") as file:
    file.write("### Retrieve Operation\n")
    file.write("Command:\n")
    file.write("book = Book.objects.get(title='1984')\n")
    file.write("Output:\n")
    file.write(f"Title: {book.title}, Author: {book.author}, Publication Year: {book.publication_year}\n")
