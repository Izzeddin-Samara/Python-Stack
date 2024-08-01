from django.db import models
import re
import bcrypt
from django.shortcuts import get_object_or_404

class UserManager(models.Manager):
    def register_validator(self, postData):
        errors = {}
        email_check = User.objects.filter(email=postData['email'])
        if email_check.exists():
            errors["email"] = "Email must be unique"
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(postData['email']):
            errors['email_error'] = "Invalid email!"
        if len(postData['first_name']) < 2:
            errors["first_name"] = "First name should be at least 2 characters"
        if len(postData['last_name']) < 2:
            errors["last_name"] = "Last name should be at least 2 characters"
        if len(postData['password']) < 8:
            errors["password"] = "Password should be at least 8 characters"
        if postData['password'] != postData['password_confirmation']:
            errors["password_confirmation"] = "Passwords do not match"
        return errors

class BookManager(models.Manager):
    def add_book_validator(self, postData):
        errors = {}
        if 'title' not in postData or not postData['title'].strip():
            errors["title"] = "Title is required"
        elif len(postData['title'].strip()) < 2:
            errors["title"] = "Title should be at least 2 characters"
       
        if len(postData['description']) < 5:
            errors["description"] = "Description should be at least 5 characters"
        return errors
    
class User(models.Model):
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    email = models.CharField(max_length=45)
    password = models.CharField(max_length=255)
    objects = UserManager()

class Book(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    uploaded_by = models.ForeignKey(User, related_name="books_uploaded", on_delete=models.CASCADE)
    users_who_like = models.ManyToManyField(User, related_name="liked_books")
    objects = BookManager()

def add_user(postData):
    pw_hash = bcrypt.hashpw(postData['password'].encode(), bcrypt.gensalt()).decode()
    user = User.objects.create(
        first_name=postData['first_name'],
        last_name=postData['last_name'],
        email=postData['email'],
        password=pw_hash
    )
    return user

def add_book(request):
    user = User.objects.get(id=request.session['userid'])
    title = request.POST['title']
    description = request.POST['description']
    uploaded_by = user
    book = Book.objects.create(title=title, description=description, uploaded_by=uploaded_by)
    return book

def update_book(postData, id):
    book = get_object_or_404(Book, id=id)
    book.title = postData['title']
    book.description = postData['description']
    book.save()

def show_all_books():
    return Book.objects.all()

def add_favorite(request, id):
    book = Book.objects.get(id=id)
    user = User.objects.get(id=request.session['userid'])
    user.liked_books.add(book)

def delete_book(id):
    book = get_object_or_404(Book, id=id)
    book.delete()

def get_book(id):
    book = Book.objects.get(id=id)
    return book

def check(postData):
    return User.objects.filter(email=postData['email']).first()

def add_to_favorites(user_id, book_id):
    user = User.objects.get(id=user_id)
    book = Book.objects.get(id=book_id)
    user.liked_books.add(book)
    user.save()

def remove_from_favorites(user_id, book_id):
    user = User.objects.get(id=user_id)
    book = Book.objects.get(id=book_id)
    user.liked_books.remove(book)
    user.save()

def get_user_favorites(user_id):
    user = User.objects.get(id=user_id)
    return user.liked_books.all()

def get_user(user_id):
    return User.objects.get(id=user_id)
