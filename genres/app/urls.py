from django.urls import path
from . import views

urlpatterns = [
    path('genres/', views.genre_list, name='genre_list'),
    path('artists/', views.artist_list, name='artist_list'),
    path('<int:artist_id>/', views.artist_detail, name='artist_detail'),
]
