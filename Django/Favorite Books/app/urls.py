from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('success/', views.success, name='success'),
    path('books/', views.books_list, name='books_list'),
    path('books/add/', views.add_book, name='add_book'),
    path('books/<int:id>/', views.book_detail, name='book_detail'),
    path('books/<int:id>/update/', views.book_update, name='book_update'),
    path('books/<int:id>/delete/', views.book_delete, name='book_delete'),
    path('books/<int:id>/add_favorite/', views.add_favorite, name='add_favorite'),
    path('books/<int:id>/remove_favorite/', views.remove_favorite, name='remove_favorite'),
    path('user_favorites/', views.user_favorites, name='user_favorites'),
    path('logout/', views.logout, name='logout'),
]
