from django.shortcuts import render, redirect
import random
from .models import Leaderboard

def index(request):
    if 'number' not in request.session:
        request.session['number'] = random.randint(1, 100)
        request.session['attempts'] = 0
    return render(request, 'index.html')

def guess(request):
    if request.method == 'POST':
        guess = int(request.POST['guess'])
        request.session['attempts'] += 1
        attempts = request.session['attempts']

        if guess < request.session['number']:
            message = "Too low!"
            color = "red"
        elif guess > request.session['number']:
            message = "Too high!"
            color = "red"
        else:
            message = f"{guess} was the number!"
            color = "green"
            return render(request, 'success.html', {
                'message': message,
                'color': color,
                'attempts': attempts,
            })

        if attempts >= 5:
            return render(request, 'lose.html')

        return render(request, 'index.html', {
            'message': message,
            'color': color,
            'attempts': attempts,
        })
    return redirect('/')

def play_again(request):
    request.session.flush()
    return redirect('/')

def leaderboard(request):
    leaders = Leaderboard.objects.all().order_by('attempts', 'date')
    return render(request, 'leaderboard.html', {'leaders': leaders})

def save_winner(request):
    if request.method == 'POST':
        name = request.POST['name']
        attempts = request.session['attempts']
        Leaderboard.objects.create(name=name, attempts=attempts)
        return redirect('/leaderboard')
    return redirect('/')
