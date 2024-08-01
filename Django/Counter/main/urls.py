from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('destroy_session', views.destroy_session, name='destroy_session'),
    path('increment_by_two', views.increment_by_two, name='increment_by_two'),
]
