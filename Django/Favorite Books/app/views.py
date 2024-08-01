from django.shortcuts import render, redirect
from django.contrib import messages
from . import models
import bcrypt

def index(request):
    return render(request, 'index.html')

def check_credentials(request):
    errors = models.User.objects.register_validator(request.POST)
    if errors:
        for key, value in errors.items():
            messages.error(request, value)
    return errors

def register(request):
    if request.method == 'POST':
        errors = check_credentials(request)
        if errors:
            return redirect('/')
        else:
            user = models.add_user(request.POST)
            messages.success(request, "Registered successfully")
            request.session['userid'] = user.id
            return redirect('/success')
    return redirect('/')

def login(request):
    if request.method == 'POST':
        user = models.check(request.POST)
        if user:
            if bcrypt.checkpw(request.POST['password'].encode(), user.password.encode()):
                request.session['userid'] = user.id
                messages.success(request, "Login successful")
                return redirect('/success')
            else:
                messages.error(request, "Invalid password")
        else:
            messages.error(request, "Email not found")
    return redirect('/')

def success(request):
    if 'userid' in request.session:
        user_id = request.session['userid']
        user = models.get_user(user_id)
        books = models.show_all_books()
        return render(request, 'success.html', {'user': user, 'books': books})
    return redirect('/')

def books_list(request):
    if 'userid' in request.session:
        user_id = request.session['userid']
        user = models.get_user(user_id)
        books = models.show_all_books()
        return render(request, 'books_list.html', {'user': user, 'books': books})
    return redirect('/')

def add_book(request):
    if request.method == 'POST':
        errors = models.Book.objects.add_book_validator(request.POST)
        if errors:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect('/books/')
        else:
            models.add_book(request)
    return redirect('/books/')

def book_detail(request, id):
    if 'userid' in request.session:
        user_id = request.session['userid']
        user = models.get_user(user_id)
        book = models.get_book(id)
        return render(request, 'book_detail.html', {'user': user, 'book': book})
    return redirect('/')

def book_update(request, id):
    if request.method == 'POST':
        models.update_book(request.POST, id)
    return redirect('/books/')

def book_delete(request, id):
    if request.method == 'POST':
        models.delete_book(id)
    return redirect('/books/')

def add_favorite(request, id):
    if 'userid' in request.session:
        user_id = request.session['userid']
        models.add_to_favorites(user_id, id)
    return redirect('/books/')

def remove_favorite(request, id):
    if 'userid' in request.session:
        user_id = request.session['userid']
        models.remove_from_favorites(user_id, id)
    return redirect('/books/')

def user_favorites(request):
    if 'userid' in request.session:
        user_id = request.session['userid']
        user = models.get_user(user_id)
        favorite_books = models.get_user_favorites(user_id)
        return render(request, 'user_favorites.html', {'user': user, 'favorite_books': favorite_books})
    return redirect('/')

def logout(request):
    request.session.flush()
    return redirect('/')
