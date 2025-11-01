from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def movies(request):
    context = [
        {"title": "The SpongeBob Movie: Sponge Out of Water", "rating": 8.1},
        {"title": "It", "rating": 7.3},
        {"title": "Iron Man 3", "rating": 7.1},
    ]

    return render(request, 'films.html', { "context": context })
