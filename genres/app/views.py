from django.shortcuts import render
from .models import Genre, Artist

def genre_list(request):
    genres = Genre.objects.all()
    return render(request, 'app/genre_list.html', {'genres': genres})

def artist_list(request):
    artists = Artist.objects.all()
    return render(request, 'app/artist_list.html', {'artists': artists})

def artist_detail(request, artist_id):
    artist = Artist.objects.get(id=artist_id)
    return render(request, 'app/artist_detail.html', {'artist': artist})
