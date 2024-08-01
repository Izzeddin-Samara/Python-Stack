from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('shows/', views.show_list, name='show_list'),
    path('shows/new/', views.show_new, name='show_new'),
    path('shows/create/', views.show_create, name='show_create'),
    path('shows/<int:id>/', views.show_detail, name='show_detail'),
    path('shows/edit/<int:id>/', views.show_edit, name='show_edit'),
    path('shows/update/<int:id>/', views.show_update, name='show_update'),
    path('shows/delete/<int:id>/', views.show_delete, name='show_delete'),
]
