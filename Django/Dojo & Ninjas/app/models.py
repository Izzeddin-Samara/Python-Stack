from django.db import models
from django.shortcuts import get_object_or_404

class Dojo(models.Model):
    name = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=2)

class Ninja(models.Model):
    dojo = models.ForeignKey(Dojo, related_name="ninjas", on_delete=models.CASCADE)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)

def show_all_Dojos():
    return Dojo.objects.all()

def create_dojo(Izz):
    name = Izz['name']
    city = Izz['city']
    state = Izz['state']
    Dojo.objects.create(name=name, city=city, state=state)

def create_ninja(Izz):
    first_name = Izz['first_name']
    last_name = Izz['last_name']
    dojo_id = Izz['dojo_id']
    dojo = get_object_or_404(Dojo, id=dojo_id)
    Ninja.objects.create(dojo=dojo, first_name=first_name, last_name=last_name)
