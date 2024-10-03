from django.db import models
from django.shortcuts import get_object_or_404


class Book(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Author(models.Model):
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    notes = models.TextField()
    books = models.ManyToManyField(Book, related_name="authors")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


def show_all_books():
    return Book.objects.all()


def add_book(post_data):
    title = post_data['title']
    description = post_data['description']
    Book.objects.create(title=title, description=description)


def add_author(post_data):
    first_name = post_data['first_name']
    last_name = post_data['last_name']
    notes = post_data['notes']
    Author.objects.create(first_name=first_name, last_name=last_name, notes=notes)


def show_all_authors():
    return Author.objects.all()


def book_view(request, book_id):
    book = Book.objects.get(id=book_id)
    author_id = request.POST.get('author_id')
    author = Author.objects.get(id=author_id)
    book.authors.add(author)


def author_view(request, author_id):
    author = Author.objects.get(id=author_id)
    book_id = request.POST.get('book_id')
    book = Book.objects.get(id=book_id)
    author.books.add(book)


def get_all_authors_exclude(book_id):
    book = Book.objects.get(id=book_id)
    all_authors = show_all_authors().exclude(id__in=book.authors.all().values_list('id', flat=True))
    return all_authors

def get_all_books_exclude(author_id):
    author = Author.objects.get(id=author_id)
    all_books = show_all_books().exclude(id__in=author.books.all().values_list('id', flat=True))
    return all_books


def get_book(book_id):
    return Book.objects.get(id=book_id)

def get_author(author_id):
    return Author.objects.get(id=author_id)