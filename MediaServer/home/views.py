from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import redirect

# Create your views here.

def firstpage(request):
    template = loader.get_template('home.html')
    movies = [
        {'title': 'Movie 1', 'year': 2022, 'genre': 'Action'},
        {'title': 'Movie 2', 'year': 2021, 'genre': 'Comedy'},
        {'title': 'Movie 3', 'year': 2020, 'genre': 'Drama'},
        # ... add more movies to the list
    ]

    context = {'movies': movies}
    return HttpResponse(template.render(context, request))

def homepage(request):
    return HttpResponse("Hello World")

def toggle_theme(request):
    if request.session.get('theme') == 'dark':
        request.session['theme'] = 'light'
    else:
        request.session['theme'] = 'dark'
     # Get the referring URL (the URL where the "Toggle Theme" link was clicked)
    referring_url = request.META.get('HTTP_REFERER', 'homepage')  # Use 'homepage' as default

    return redirect(referring_url)  # Redirect back to the referring URL