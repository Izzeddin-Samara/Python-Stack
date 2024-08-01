from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('process_money/<str:location>/', views.process_money, name='process_money'),
    path('set_conditions/', views.set_conditions, name='set_conditions'),
]
