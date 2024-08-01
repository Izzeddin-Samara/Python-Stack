from django.shortcuts import render, redirect, get_object_or_404
from . import models
from .models import Dojo 

def index(request):
    dojos = models.show_all_Dojos()
    context = {
        "dojos": dojos
    }
    return render(request, "index.html", context)

def add_dojo(request):
    if request.method == 'POST':
        models.create_dojo(request.POST)
        return redirect('index')

def add_ninja(request):
    if request.method == 'POST': 
        models.create_ninja(request.POST)  
        return redirect('index')

def delete_dojo(request, dojo_id):
    dojo = get_object_or_404(Dojo, id=dojo_id)
    dojo.delete()
    return redirect('index')
