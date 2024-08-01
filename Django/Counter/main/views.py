from django.shortcuts import render, redirect

def index(request):
    if 'counter' not in request.session:
        request.session['counter'] = 0
    if 'visits' not in request.session:
        request.session['visits'] = 0

    request.session['visits'] += 1

    if request.method == 'POST':
        increment = int(request.POST.get('increment', 1))
        request.session['counter'] += increment

    context = {
        'counter': request.session['counter'],
        'visits': request.session['visits']
    }
    return render(request, 'index.html', context)

def destroy_session(request):
    request.session.flush()
    return redirect('index')

def increment_by_two(request):
    if 'counter' in request.session:
        request.session['counter'] += 2
    else:
        request.session['counter'] = 2
    return redirect('index')
