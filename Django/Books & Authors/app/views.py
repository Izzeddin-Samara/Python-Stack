from django.shortcuts import render, redirect, get_object_or_404
from . import models
from .models import Book, Author

def index(request):
    all_the_books = models.show_all_books()
    return render(request, 'index.html', {'all_the_books': all_the_books})

def add_book(request):
    if request.method == 'POST':
        models.add_book(request.POST)
        return redirect('index')
    all_the_books = models.show_all_books()
    return render(request, 'index.html', {'all_the_books': all_the_books})



def book_view(request, book_id):
    if request.method == 'POST':
        models.book_view(request, book_id)
    context ={
        'all_authors': models.get_all_authors_exclude(book_id),
        'book': models.get_book(book_id)
    }
    return render(request, 'book_view.html', context)

def add_author(request):
    if request.method == 'POST':
        models.add_author(request.POST)
        return redirect('add_author')
    all_the_authors = models.show_all_authors()
    return render(request, 'add_author.html', {'all_the_authors': all_the_authors})



def author_view(request, author_id):
    if request.method == 'POST':
        models.author_view(request, author_id)
    context ={
        'all_books': models.get_all_books_exclude(author_id),
        'author': models.get_author(author_id)
    }
    return render(request, 'author_view.html', context)
