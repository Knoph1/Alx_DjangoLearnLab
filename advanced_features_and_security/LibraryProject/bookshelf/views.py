from django.shortcuts import render

# Create your views here.
from django.contrib.auth.decorators import permission_required
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseForbidden
from .models import Article

@permission_required('myapp.can_view', raise_exception=True)
def article_list(request):
    articles = Article.objects.all()
    return render(request, 'articles/list.html', {'articles': articles})

@permission_required('myapp.can_create', raise_exception=True)
def article_create(request):
    if request.method == 'POST':
        # Form handling logic
        return redirect('article_list')
    return render(request, 'articles/create.html')

@permission_required('myapp.can_edit', raise_exception=True)
def article_edit(request, pk):
    article = get_object_or_404(Article, pk=pk)
    if request.method == 'POST':
        # Edit logic
        return redirect('article_list')
    return render(request, 'articles/edit.html', {'article': article})

@permission_required('myapp.can_delete', raise_exception=True)
def article_delete(request, pk):
    article = get_object_or_404(Article, pk=pk)
    article.delete()
    return redirect('article_list')
# Enforcing permissions using @permission_required
# Example: Only users with 'can_edit' permission can access article_edit view.
from django.shortcuts import render, get_object_or_404
from .models import Book

# Displays a list of all books
def book_list(request):
    books = Book.objects.all()  # Fetch all books from the database
    return render(request, 'bookshelf/book_list.html', {'books': books})

# Displays details for a single book
def books(request, book_id):
    book = get_object_or_404(Book, id=book_id)  # Fetch the specific book or raise a 404
    return render(request, 'bookshelf/book_detail.html', {'book': book})

from django.shortcuts import render
from .forms import ExampleForm

def example_view(request):
    if request.method == 'POST':
        form = ExampleForm(request.POST)
        if form.is_valid():
            # Process the data
            field_data = form.cleaned_data['field_name']
            # Add your logic here
    else:
        form = ExampleForm()

    return render(request, 'bookshelf/example_form.html', {'form': form})
