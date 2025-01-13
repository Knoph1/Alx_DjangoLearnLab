# Update the book title

book.title = "Nineteen Eighty-Four"
book.save()

# Documenting in update.md

with open("update.md", "w") as file:
    file.write("### Update Operation\n")
    file.write("Command:\n")
    file.write("book.title = 'Nineteen Eighty-Four'\n")
    file.write("book.save()\n")
    file.write("Output:\n")
    file.write("Successfully updated Book title to 'Nineteen Eighty-Four'.\n")
