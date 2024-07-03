from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def result(request):
    # Access POST data directly from the request.POST dictionary
    name = request.POST['name']
    location = request.POST['location']
    language = request.POST['language']
    contact = request.POST['contact']
    hobbies = request.POST.getlist('hobbies')  # Get multiple checkbox values
    hobbies_str = ", ".join(hobbies)  # Convert list to string
    comment = request.POST['comment']
    
    context = {
        'name': name,
        'location': location,
        'language': language,
        'contact': contact,
        'hobbies': hobbies_str,
        'comment': comment,
    }
    
    return render(request, 'result.html', context)

