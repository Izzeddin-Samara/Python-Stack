from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add_book/', views.add_book, name='add_book'),
    path('book/<int:book_id>/', views.book_view, name='book_view'),
    path('authors/', views.add_author, name='add_author'), 
    path('author/<int:author_id>/', views.author_view, name='author_view'),
]
