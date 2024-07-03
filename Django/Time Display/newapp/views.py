from django.shortcuts import render
from time import localtime, strftime

def index(request):
    context = {
        "time": strftime("%Y-%m-%d %I:%M %p", localtime())  # %I for 12-hour format
    }
    return render(request, 'index.html', context)
