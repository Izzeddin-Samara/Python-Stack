from django.shortcuts import render, redirect
import random
from datetime import datetime

def index(request):
    if 'gold' not in request.session:
        request.session['gold'] = 0
    if 'activities' not in request.session:
        request.session['activities'] = []
    if 'moves' not in request.session:
        request.session['moves'] = None
    if 'goal' not in request.session:
        request.session['goal'] = None

    context = {
        'gold': request.session['gold'],
        'moves': request.session['moves'],
        'goal': request.session['goal'],
        'activities': request.session['activities'],
        'win': False,
        'lose': False,
    }

    # Check win/loss conditions
    if request.session['moves'] == 0:
        if request.session['gold'] >= 0:
            context['win'] = True
        else:
            context['lose'] = True

    return render(request, 'index.html', context)

def process_money(request, location):
    if location == 'farm':
        gold_earned = random.randint(10, 20)
    elif location == 'cave':
        gold_earned = random.randint(5, 10)
    elif location == 'house':
        gold_earned = random.randint(2, 5)
    elif location == 'quest':
        gold_earned = random.randint(-50, 50)

    request.session['gold'] += gold_earned
    activity_class = 'earn' if gold_earned >= 0 else 'lose'
    activity = {
        'activity': f"Earned {gold_earned} golds from the {location}!" if gold_earned >= 0 else f"Lost {abs(gold_earned)} golds at the {location}!",
        'timestamp': datetime.now().strftime('%Y/%m/%d %I:%M %p'),
        'class': activity_class
    }
    request.session['activities'].append(activity)
    request.session.modified = True

    if request.session['moves'] is not None:
        request.session['moves'] -= 1

    return redirect('/')

def set_conditions(request):
    if request.method == 'POST':
        # Clear previous game session data
        request.session.flush()
        
        # Initialize new game session data
        request.session['gold'] = 0
        request.session['activities'] = []
        request.session['moves'] = int(request.POST['moves'])
        request.session['goal'] = int(request.POST['goal'])
        return redirect('/')
