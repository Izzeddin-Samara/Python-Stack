from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Show
from datetime import datetime

def check_credentials(request, show_id=None):
    errors = Show.objects.basic_validator(request.POST, show_id=show_id)
    if errors:
        for key, value in errors.items():
            messages.error(request, value)
    return errors

def show_create(request):
    if request.method == 'POST':
        errors = check_credentials(request)
        if errors:
            return redirect('/shows/new')
        else:
            Show.create_show(request)
            messages.success(request, "Show successfully created")
            return redirect('/shows')


def show_update(request, id):
    show = get_object_or_404(Show, id=id)
    if request.method == 'POST':
        errors = check_credentials(request, show_id=show.id)
        if errors:
            return redirect(f'/shows/edit/{show.id}')
        else:
            Show.update_show(request, show.id)
            messages.success(request, "Show successfully updated")
            return redirect(f'/shows/{show.id}')
    

def index(request):
    return redirect('/shows')

def show_list(request):
    shows = Show.objects.all()
    return render(request, 'show_list.html', {'shows': shows})

def show_detail(request, id):
    show = get_object_or_404(Show, id=id)
    formatted_date = show.release_date.strftime('%Y-%m-%d')
    return render(request, 'show_detail.html', {'show': show, 'formatted_date': formatted_date})

def show_new(request):
    return render(request, 'show_form.html')

def show_edit(request, id):
    show = get_object_or_404(Show, id=id)
    return render(request, 'update.html', {'show': show})

def show_delete(request, id):
    show = get_object_or_404(Show, id=id)
    if request.method == 'POST':
        show.delete()
        return redirect('/shows')
    return render(request, 'show_confirm_delete.html', {'show': show})
