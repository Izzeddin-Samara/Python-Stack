from django.db import models
from django.shortcuts import get_object_or_404
from django.utils import timezone

class ShowManager(models.Manager):
    def basic_validator(self, postData, show_id=None):
        errors = {}
        # Validate title uniqueness
        title_check = Show.objects.filter(title=postData['title'])
        if show_id:
            title_check = title_check.exclude(id=show_id)
        if title_check.exists():
            errors["title"] = "Title must be unique"

        # Validate title length
        if len(postData['title']) < 2:
            errors["title"] = "Title should be at least 2 characters"

        # Validate network length
        if len(postData['network']) < 3:
            errors["network"] = "Network should be at least 3 characters"

        # Validate description length if it exists
        if 'description' in postData and postData['description'] and len(postData['description']) < 10:
            errors["description"] = "Description should be at least 10 characters if provided"

        # Validate release date is in the past
        if 'release_date' in postData and postData['release_date']:
            release_date = timezone.datetime.strptime(postData['release_date'], '%Y-%m-%d').date()
            if release_date >= timezone.now().date():
                errors["release_date"] = "Release date must be in the past"

        return errors

class Show(models.Model):
    title = models.CharField(max_length=255, unique=True)
    network = models.CharField(max_length=255)
    release_date = models.DateField()
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = ShowManager()

    
    def create_show(request):
        title = request.POST.get('title')
        network = request.POST.get('network')
        release_date = request.POST.get('release_date')
        description = request.POST.get('description')
        new_show = Show.objects.create(title=title, network=network, release_date=release_date, description=description)
        return new_show

    
    def update_show(request, id):
        show = get_object_or_404(Show, id=id)
        show.title = request.POST.get('title')
        show.network = request.POST.get('network')
        show.release_date = request.POST.get('release_date')
        show.description = request.POST.get('description')
        show.save()
        return show
def show_all_shows():
    return Show.objects.all()



def delete_show(show_id):
    show = get_object_or_404(Show, id=show_id)
    show.delete()
    return show

